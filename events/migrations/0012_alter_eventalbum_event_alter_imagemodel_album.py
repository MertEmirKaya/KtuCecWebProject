# Generated by Django 4.0.3 on 2022-04-10 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_imagemodel_event_eventalbum_imagemodel_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventalbum',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='events.eventmodel'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.eventalbum'),
        ),
    ]
