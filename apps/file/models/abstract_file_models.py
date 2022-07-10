import uuid

from django.db import models

from apps.file.managers import FileManager


class AbstractFileModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    original_name = models.TextField(default=None, blank=True, help_text="Original name")

    core = models.FileField()

    md5sum = models.CharField(max_length=32, null=True, default=None)
    meta = models.JSONField(default=dict)

    creator = models.ForeignKey(
        'user.User',
        on_delete=models.SET_DEFAULT,
        related_name='%(class)s_created',
        null=True,
        default=None
    )

    removed_from_storage = models.BooleanField(default=False, db_index=True)
    is_public = models.BooleanField(default=True, db_index=True)
    is_optimized = models.BooleanField(default=False, db_index=True)

    ######### GenericForeignKey is not a good idea to use, instead we are using abstract idea ##########
    # # GenericForeignKey
    # owner_id = models.PositiveIntegerField()
    # owner_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    # owner = GenericForeignKey('owner_type', 'owner_id')
    ####################################################################################################

    create_date = models.DateTimeField(auto_now_add=True)

    objects = FileManager()

    def __str__(self):
        return self.original_name

    class Meta:
        ordering = ['-create_date']
        abstract = True
