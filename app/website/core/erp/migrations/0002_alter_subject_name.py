# Generated by Django 4.2.3 on 2023-08-21 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50, verbose_name='materia'),
        ),
    ]
