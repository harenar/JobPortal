# Generated by Django 4.1.6 on 2023-05-06 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0002_alter_jobpost_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobportal.employee', unique=True),
        ),
    ]
