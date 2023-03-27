# Generated by Django 3.2.5 on 2023-03-27 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notebooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(blank=True, max_length=128)),
                ('session_id', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('params', models.TextField(blank=True)),
                ('result', models.TextField(blank=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebooks.notebook')),
            ],
        ),
    ]
