# Generated by Django 3.2.11 on 2022-05-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_section_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='media_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
