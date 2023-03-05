# Generated by Django 3.2.1 on 2023-03-04 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='', max_length=2048, verbose_name='Task')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')),
                ('insert_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
