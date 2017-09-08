import json
import falcon
import time
import uuid
import requests
from apps.database import init_db, db_session
from apps.models import Account

from apps.restaccount.logging import logging
logger = logging.getLogger(__name__)

from decouple import config

ES_HOST = config('EVENTSTORE_HOST', default='eventstore')
ES_PORT = config('EVENTSTORE_PORT', default=2113, cast=int)

stream_url = 'http://{}:{}/streams/accounts'.format(ES_HOST, ES_PORT)
content_header = { 'Content-Type': 'application/vnd.eventstore.events+json' }

logger.info('stream_url: {}'.format(stream_url))

def get_account(account_id):
    return Account.query.get(account_id)

class BalanceResource(object):

    def on_get(self, req, resp, account_id):
        init_db()
        doc = db_session.query(Account).get(account_id)
        db_session.close()

        if doc is None:
            raise falcon.HTTPBadRequest('Balance missing', 'Deposit money to start using an account')
        else:
            # Create a JSON representation of the resource
            resp.body = json.dumps(doc.as_dict(), ensure_ascii=False)
            # The following line can be omitted because 200 is the default
            # status returned by the framework, but it is included here to
            # illustrate how this may be overridden as needed.
            resp.status = falcon.HTTP_200

class DepositResource(object):

    def on_post(self, req, resp):
        body = req.stream.read()
        doc = json.loads(body.decode('utf-8'))

        logger.info('doc: {}'.format(doc))
        
        payload = [
          {
            "eventId": str(uuid.uuid1()),
            "eventType": "created-deposit",
            "data": doc
          }
        ]

        logger.info("payload: {}".format(payload))

        r = requests.post(stream_url, data=str(payload), headers=content_header)

        resp.status = falcon.HTTP_200

class TransferResource(object):

    def on_post(self, req, resp):
        body = req.stream.read()
        doc = json.loads(body.decode('utf-8'))

        acc = get_account(doc['account_id'])
        
        payload = [
          {
            "eventId": str(uuid.uuid1()),
            "eventType": "created-transfer",
            "data": doc
          }
        ]

        if acc is None:
            raise falcon.HTTPBadRequest('Account missing', 'You must deposit into an account before transfering')
        if acc.balance < doc['amount']:
            raise falcon.HTTPBadRequest('Insufficient funds', 'Account balance {} less than transfer amount {}'.format(acc.balance, doc['amount']))
        else:
            logger.info("payload: {}".format(payload))
            r = requests.post(stream_url, data=str(payload), headers=content_header)
            resp.status = falcon.HTTP_200