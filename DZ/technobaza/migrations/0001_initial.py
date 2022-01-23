# Generated by Django 4.0.1 on 2022-01-21 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('diag', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='technobaza.manufacturer')),
            ],
        ),
    ]
