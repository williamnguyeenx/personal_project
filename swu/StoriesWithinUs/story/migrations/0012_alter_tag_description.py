# Generated by Django 4.2.3 on 2023-08-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0011_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(default='0'),
        ),
    ]
