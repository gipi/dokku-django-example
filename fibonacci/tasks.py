from __future__ import absolute_import
import logging
from celery import shared_task
from celery.task import periodic_task
from datetime import timedelta
from .models import Fibonacci

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('tasks_info')

logger.info(' * tasks')


def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

@periodic_task(run_every=timedelta(seconds=10))
def print_fib():
    f, created = Fibonacci.objects.get_or_create(pk=1)
    logger.info('fibonacci of %d: %d' % (f.last_number, fib(f.last_number)))
    f.last_number += 1
    f.save()
