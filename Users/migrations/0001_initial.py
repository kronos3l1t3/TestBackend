# Generated by Django 3.2.1 on 2023-03-05 16:45

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
            name='ProfileImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to=settings.AUTH_USER_MODEL, verbose_name='User Images')),
            ],
        ),
    ]
