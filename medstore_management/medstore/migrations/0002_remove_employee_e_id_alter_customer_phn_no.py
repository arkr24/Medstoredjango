# Generated by Django 4.2.4 on 2023-09-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='e_id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phn_no',
            field=models.BigIntegerField(unique=True),
        ),
    ]
