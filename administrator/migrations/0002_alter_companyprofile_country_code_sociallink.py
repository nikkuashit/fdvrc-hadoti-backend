# Generated by Django 4.0 on 2021-12-22 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='country_code',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.companyprofile')),
            ],
            options={
                'verbose_name_plural': 'Social Link',
            },
        ),
    ]
