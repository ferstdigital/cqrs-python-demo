# app.py
# AtomicPuppy uses asyncio coroutines for concurrent IO
import asyncio
import signal
from atomicpuppy import AtomicPuppy
import sys
from decouple import config
from apps.readaccount.logger import logging
from apps.readaccount.processors import process_deposit, process_transfer

logger = logging.getLogger(__name__)

# AtomicPuppy needs a callback to pass you messages.
def handle(event):
    if event.stream == 'accounts' and event.type == 'created-deposit':
        return process_deposit(event)
    elif event.stream == 'accounts' and event.type == 'created-transfer':
        return process_transfer(event)
    logger.info('handle event: {}'.format(vars(event)))
    return

cfg = {
    'atomicpuppy': {
        'host': config('EVENTSTORE_HOST', default='eventstore'),
        'port': config('EVENTSTORE_PORT', default=2113, cast=int),
        'streams': ['accounts']
    }
}

# Config is read from yaml files.
ap = AtomicPuppy(cfg, handle)
loop = asyncio.get_event_loop()

# to kill the puppy, call stop()
def stop():
    logger.debug("SIGINT received, shutting down")
    ap.stop()
    sys.exit()

loop.add_signal_handler(signal.SIGINT, stop)

# and to start it call start.
loop.run_until_complete(ap.start())