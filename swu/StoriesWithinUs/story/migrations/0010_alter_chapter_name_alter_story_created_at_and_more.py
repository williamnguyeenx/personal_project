# Generated by Django 4.2.3 on 2023-08-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_alter_story_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(),
        ),
    ]
