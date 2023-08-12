from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','planrcomm.settings')

app = Celery('celery_app')

app.config_from_object('celery_config', namespace='CELERY')

app.conf.task_queues = (
    app.conf.task_queues + (
        {
            "name": "tasks_queue",
            "routing_key": "tasks",
        },
        {
            "name": "results_queue",
            "routing_key": "results",
        },
    )
)

app.autodiscover_tasks()
