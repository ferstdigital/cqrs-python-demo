import logging
import os
from logging.handlers import TimedRotatingFileHandler

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# set up logging to file
logging.basicConfig(
     filename='logs/server.log',
     level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
# logging.getLogger('').addHandler(TimedRotatingFileHandler)

# logger = logging.getLogger(__name__)