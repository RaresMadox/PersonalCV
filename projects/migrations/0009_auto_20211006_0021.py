# Generated by Django 3.2.7 on 2021-10-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_rename_tags_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumb1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumb2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumb3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]