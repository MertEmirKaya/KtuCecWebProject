# Generated by Django 4.0.3 on 2022-04-10 15:59

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_eventmodel_available_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=events.models.upload_to)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventmodel')),
            ],
        ),
    ]