from django.db import migrations

def add_default_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    Category.objects.get_or_create(name='Mental Health')
    Category.objects.get_or_create(name='Heart Disease')
    Category.objects.get_or_create(name='Covid19')
    Category.objects.get_or_create(name='Immunization')

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),  # Your first migration
    ]

    operations = [
        migrations.RunPython(add_default_categories),
    ]