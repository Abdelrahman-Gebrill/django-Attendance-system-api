# Generated by Django 4.0 on 2021-12-23 22:05

from django.db import migrations


class Migration(migrations.Migration):
    def UpdateAdminRole(apps,schema_editor):
        User = apps.get_model('authentication','User')
        admin = User.objects.get(username = "admin",)
        role = apps.get_model('role','role')
        managerRole = role.objects.get(roleName='manager')
        admin.role = managerRole
        admin.save()

    dependencies = [
        ('role', '0002_auto_20211222_0234'),
    ]

    operations = [
        migrations.RunPython(UpdateAdminRole),
    ]