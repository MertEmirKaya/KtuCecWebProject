# Generated by Django 4.0.3 on 2022-08-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_rename_departmand_profilemodel_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
