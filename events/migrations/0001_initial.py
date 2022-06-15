# Generated by Django 4.0.3 on 2022-06-15 08:10

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventAlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organizer', models.CharField(blank=True, max_length=100, null=True)),
                ('events_date', models.DateTimeField()),
                ('announcement_date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('statement', models.TextField()),
                ('content', models.CharField(blank=True, max_length=90)),
                ('is_ready', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=events.models.upload_to)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='events.eventalbummodel')),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=events.models.upload_to)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.eventalbummodel')),
            ],
        ),
        migrations.AddField(
            model_name='eventalbummodel',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='events.eventmodel'),
        ),
    ]
