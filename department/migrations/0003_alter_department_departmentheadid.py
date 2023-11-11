# Generated by Django 4.0 on 2021-12-20 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_user_department'),
        ('department', '0002_alter_department_departmentheadid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='departmentHeadID',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='headOnDepartment', to='authentication.user'),
        ),
    ]
