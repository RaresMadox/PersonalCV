# Generated by Django 3.2.7 on 2021-10-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20211006_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category2',
        ),
    ]
