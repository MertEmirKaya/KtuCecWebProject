# Generated by Django 4.0.3 on 2022-03-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_profilemodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='password1',
            field=models.CharField(default=123456, max_length=20),
            preserve_default=False,
        ),
    ]
