# Generated manually to fix foreign key references

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_section_media_file'),
    ]

    operations = [
        # These operations only update the field definitions in Django's metadata
        # The actual database data is already correct (IDs instead of titles)
        migrations.AlterField(
            model_name='section',
            name='component_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='core.componenttype'),
        ),
        migrations.AlterField(
            model_name='section',
            name='core_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='core.corepage'),
        ),
    ]