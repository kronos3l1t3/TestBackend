# Generated by Django 4.1.7 on 2023-03-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimages',
            name='image',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
