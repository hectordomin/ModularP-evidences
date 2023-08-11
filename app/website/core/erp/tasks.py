from __future__ import absolute_import
from daemon import app
import time
from celery import shared_task

@shared_task
def add(x, y):
    # sleep 5 seconds
    time.sleep(5)
    print(f'working with {x} and {y}')
    return x + y