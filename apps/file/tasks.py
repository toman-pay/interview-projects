import logging
import os
import shutil

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def remove_file_from_local_storage(path):
    pass
