# Generated by Django 4.0.3 on 2022-03-26 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_rename_eventsmodel_eventmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='user_who_attend',
            field=models.ManyToManyField(related_name='users_who_attend', to=settings.AUTH_USER_MODEL),
        ),
    ]