# Generated by Django 4.2.3 on 2023-08-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
