# Generated by Django 4.0.3 on 2022-04-10 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_videomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='events.eventalbummodel'),
            preserve_default=False,
        ),
    ]
