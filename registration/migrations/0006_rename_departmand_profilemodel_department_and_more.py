# Generated by Django 4.0.3 on 2022-07-21 08:48

import django.contrib.auth.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_profilemodel_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='departmand',
            new_name='department',
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='username',
            field=models.CharField(default=uuid.uuid4, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]