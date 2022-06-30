import arrow
from django.db import models

from escrow.models import BaseModel


def images_upload_path(instance, filename):
    """This method returns images storage path"""
    return 'images/{filename}'.format(filename=filename)


class ProductModel(BaseModel):
    """Product Model"""
    title = models.CharField(max_length=125, null=False, blank=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(max_length=1024, null=False, blank=False)

    @staticmethod
    def _regenerate_field_for_soft_deletion(obj, field_name):
        timestamp = arrow.utcnow().timestamp
        max_length = obj.__class__._meta.get_field(field_name).max_length
        slug_suffix = '-deleted-{}'.format(str(timestamp))
        new_slug = getattr(obj, field_name)

        if (len(new_slug) + len(slug_suffix)) > max_length:
            cutoff = max_length - len(slug_suffix)
            new_slug = obj.slug[:cutoff]
        return new_slug + slug_suffix

    def delete(self):
        # Rename the product to prevent collisions
        self.title = self._regenerate_field_for_soft_deletion(self, 'title')
        # SoftDeletionModel.delete() saves the object, so no need to save it here
        return super(ProductModel, self).delete()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"


class ProductImageModel(BaseModel):
    """Image Model"""
    image = models.ImageField(upload_to=images_upload_path, blank=False, null=False, editable=False)
    product = models.ForeignKey(to=ProductModel, to_field='id', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        db_table = "images"
