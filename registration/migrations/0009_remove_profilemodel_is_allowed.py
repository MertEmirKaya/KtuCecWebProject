# Generated by Django 4.0.3 on 2022-10-03 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_profilemodel_is_allowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='is_allowed',
        ),
    ]