# Generated by Django 4.0.3 on 2022-04-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_rename_profile_foto_profilemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='grade',
            field=models.CharField(blank=True, choices=[('Hazırlık Sınıfı', 'Hazırlık Sınıfı'), ('Birinci Sınıf', 'Birinci Sınıf'), ('İkinci Sınıf', 'İkinci Sınıf'), ('Üçüncü Sınıf', 'Üçüncü Sınıf'), ('Dördüncü Sınıf', 'Dördüncü Sınıf'), ('4+', '4+')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='school_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
