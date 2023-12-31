# Generated by Django 3.2.22 on 2024-01-03 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_auto_20240103_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignees',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='task_assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='projects.project'),
        ),
    ]
