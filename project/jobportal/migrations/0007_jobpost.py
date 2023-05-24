# Generated by Django 4.1.6 on 2023-05-10 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0006_delete_jobpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_logo', models.ImageField(blank=True, upload_to='image/')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Skills_required', models.CharField(max_length=50)),
                ('Job_salary', models.IntegerField()),
                ('Job_location', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Status', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobportal.employee')),
            ],
        ),
    ]
