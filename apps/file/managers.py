from django.db import models


class FileManager(models.Manager):
    def create(self, **kwargs):
        # TODO: get md5
        # TODO: get meta using tool like exiftool ....
        # TODO: make thumbnail (or it is possible to do it async like celery or ...)
        # TODO: generate dir that file go to wrote. Currently we are store all files in media's root dir :))))

        file = self.model(**kwargs)
        file.save(force_insert=True, using=self.db)
        return file
