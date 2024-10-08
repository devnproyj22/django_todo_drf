# Generated by Django 5.1 on 2024-08-16 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_todo_changed_at_todo_new_status_todocomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='changed_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='new_status',
        ),
        migrations.CreateModel(
            name='TodoStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.BooleanField()),
                ('new_status', models.BooleanField(default=False)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.todo')),
            ],
        ),
    ]
