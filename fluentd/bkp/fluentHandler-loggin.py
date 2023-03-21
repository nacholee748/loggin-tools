import logging
from fluent import handler

## Configure Fluentd Handler
fluentHost = "localhost"
fluentPort = 24224
fluent_handler = handler.FluentHandler(host=fluentHost, port=fluentPort,tag='fluentd.test' )
## Set format to Fluent Handler
custom_format = {
  'host': '%(hostname)s',
  'where': '%(module)s.%(funcName)s',
  'type': '%(levelname)s',
  'stack_trace': '%(exc_text)s'
}
formatter = handler.FluentRecordFormatter(custom_format)
fluent_handler.setFormatter(formatter)

## Configure python logging and loger
FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
# logging.basicConfig(filename='myapp.log', level=logging.INFO, format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('jim.log.loggin')

## Set Fluent Handler to Python logger
logger.addHandler(fluent_handler)

## Standar Python Logging with logger
logger.info('LOG DE PRUEBA JIM')
