# Generated by Django 3.2.7 on 2021-10-05 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20211005_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category1',
            new_name='category',
        ),
    ]
