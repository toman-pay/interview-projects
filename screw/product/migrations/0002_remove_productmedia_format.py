# Generated by Django 4.0.5 on 2022-06-02 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmedia',
            name='format',
        ),
    ]
