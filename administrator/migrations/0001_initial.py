# Generated by Django 4.0 on 2021-12-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('sub_title', models.CharField(blank=True, max_length=255)),
                ('sub_image', models.ImageField(blank=True, upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=5)),
                ('contact_number', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Company Profile',
            },
        ),
    ]
