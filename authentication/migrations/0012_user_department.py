# Generated by Django 4.0 on 2021-12-20 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_departmentheadid'),
        ('authentication', '0011_remove_user_date_joined_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department'),
        ),
    ]