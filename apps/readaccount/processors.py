import json
from apps.database import init_db, db_session
from apps.models import Account
from apps.readaccount.logger import logging

logger = logging.getLogger(__name__)

def init_account(account_id):
    init_db()
    if db_session.query(Account).get(account_id) is None:
        acc = Account({ 'id': account_id, 'balance': 0 })
        db_session.add(acc)
        db_session.commit()
    db_session.close()

def valid_seq(account_id, seq):
    acc = Account.query.get(account_id)
    if seq > acc.sequence:
        return True
    return False

def process_deposit(e):
    init_db()

    amount = e.data['amount']
    account_id = e.data['account_id']
    seq = e.sequence

    init_account(account_id)

    if valid_seq(account_id, seq):
        logger.info("processing deposit: {}".format(vars(e)))
        updoc = { Account.sequence: seq, Account.balance: Account.balance + amount }
        Account.query.filter_by(id=account_id).update(updoc)
        db_session.commit()
    db_session.close()
    return

def process_transfer(e):
    init_db()

    amount = e.data['amount']
    account_id = e.data['account_id']
    seq = e.sequence

    init_account(account_id)

    if valid_seq(account_id, seq):
        logger.info("processing transfer: {}".format(vars(e)))
        acc = Account.query.get(account_id)
        updoc = { Account.sequence: seq, Account.balance: Account.balance - amount }
        Account.query.filter_by(id=account_id).update(updoc)
        db_session.commit()
    db_session.close()
    return
