import logging
from fluentd_log_handler.handler import NeilFluentdHandler

handler = NeilFluentdHandler(tag='app.worker')

logger = logging.getLogger('neil')
logger.addHandler(handler)

logger.error({'message': {'task': '금융정보조회', 'company_id': 123}})