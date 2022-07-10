import os
import shutil

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def remove_file_from_local_storage_task(path):
    if os.path.isfile(path):
        os.remove(path)
        # let raise exception, bez we can't do anything if any permission denied or ... occurs during delete file :(
