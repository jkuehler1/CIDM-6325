# Generated by Django 4.2 on 2023-09-25 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('credits', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('in-progress', 'In Progress')], default='in-progress', max_length=11)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='degree_checklist.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
