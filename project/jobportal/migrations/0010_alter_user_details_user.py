# Generated by Django 4.1.6 on 2023-05-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('jobportal', '0009_user_details_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user_register'),
        ),
    ]