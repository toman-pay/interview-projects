# Generated by Django 4.0.5 on 2022-06-02 13:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_file_productmedia_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
    ]