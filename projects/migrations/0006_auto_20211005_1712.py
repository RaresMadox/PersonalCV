# Generated by Django 3.2.7 on 2021-10-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_category1_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumb1',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb2',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb3',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]