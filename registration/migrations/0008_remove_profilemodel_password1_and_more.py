# Generated by Django 4.0.3 on 2022-03-28 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_profilemodel_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='password2',
        ),
    ]
