import logging

from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)


@shared_task
def say_hi_to_toman():
    print("HIIIIIIIIIIIIIIIIIiiiIIIiIiiIi :)")
