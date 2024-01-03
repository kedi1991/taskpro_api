# Generated by Django 3.2.22 on 2024-01-03 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
        ('tasks', '0002_auto_20231012_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Executing'), (2, 'Completed'), (3, 'Blocked')], default=0),
        ),
    ]
