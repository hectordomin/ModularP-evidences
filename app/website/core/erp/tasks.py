from celery import shared_task
#from planrcomm.celery import app
import time

@shared_task(queue='request_queue')
def add(x, y):
    time.sleep(5)
    print(f'working with {x} and {y}')
    return x + y