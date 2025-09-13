from django.db import migrations

def create_entidad_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    # buscamos el content type del modelo Reporte
    ct = ContentType.objects.get(app_label='reportes', model='reporte')
    try:
        perm = Permission.objects.get(content_type=ct, codename='can_change_status')
    except Permission.DoesNotExist:
        return  # si no existe, no hacemos nada (puede que se cree luego)

    group, created = Group.objects.get_or_create(name='Entidad')
    group.permissions.add(perm)

class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_entidad_group),
    ]

