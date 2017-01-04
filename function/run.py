import os, sys, json, time
import logging

sitepackage = ".\\site-packages"
sys.path.append(sitepackage)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('function.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - [%(process)d:%(thread)d] %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.debug('function started name:{0} id:{1} time:{2}'.format(__file__, os.environ['INVOCATIONID'], time.time()))

# read the queue message and write to stdout
input = open(os.environ['input']).read()

logger.debug('read file %s' % (os.environ['input']))

try:
    provision_json = json.loads(input)
    logger.debug('before sleep {0} seconds'.format(provision_json['sleep']))
    time.sleep(provision_json['sleep'])
    logger.debug('after sleep {0} seconds'.format(provision_json['sleep']))
except (ValueError, KeyError) as inst:
    logger.error(inst)
