import json
import falcon
from apps.restaccount.resources import DepositResource, TransferResource, BalanceResource

from decouple import config

from apps.database import init_db, db_session

init_db()
db_session.close()

app = application = falcon.API(middleware=[])

app.add_route('/deposits', DepositResource())
app.add_route('/transfers', TransferResource())
app.add_route('/balances/{account_id}', BalanceResource())
