# Generated by Django 4.0.3 on 2022-07-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodel',
            name='application_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]