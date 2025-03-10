from django.db import migrations

def add_default_priorities(apps, schema_editor):
    Priority = apps.get_model('todoappGB', 'Priority')
    Priority.objects.create(name='Low', value=1)
    Priority.objects.create(name='Medium', value=2)
    Priority.objects.create(name='High', value=3)

class Migration(migrations.Migration):

    dependencies = [
        ('todoappGB', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_priorities),
    ]