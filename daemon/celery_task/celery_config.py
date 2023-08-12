CELERY_BROKER_URL = 'amqp://planercomm:planer@164.92.95.57/planercomm_vhost'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_DEFAULT_QUEUE = 'request_queue'
CELERY_IGNORE_RESULT = False