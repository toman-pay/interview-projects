import hashlib
import os
import uuid

from django.db import models


def md5(file):
    hash_md5 = hashlib.md5()
    for chunk in iter(lambda: file.read(4096), b""):
        hash_md5.update(chunk)
    return hash_md5.hexdigest()


class FileManager(models.Manager):
    def create(self, **kwargs):
        # TODO: get md5
        # TODO: get meta using tool like exiftool ....
        # TODO: make thumbnail (or it is possible to do it async like celery or ...)
        # TODO: generate dir that file go to wrote. Currently we are store all files in media's root dir :))))
        core = kwargs['core']
        md5sum = md5(core.file)
        original_name, extension = os.path.splitext(core.name or '')
        core.name = f"{uuid.uuid4()}{extension}"
        file = self.model(md5sum=md5sum, original_name=original_name, **kwargs)
        file.save(force_insert=True, using=self.db)
        return file
