# Generated by Django 4.0 on 2021-12-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(default='test.jpg', upload_to='phones/static/phones/images'),
        ),
    ]
