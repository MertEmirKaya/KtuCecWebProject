# Generated by Django 4.0.3 on 2022-04-10 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_imagemodel_event_imagemodel_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='event',
        ),
        migrations.CreateModel(
            name='EventAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='events.eventmodel')),
            ],
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.eventalbum'),
            preserve_default=False,
        ),
    ]