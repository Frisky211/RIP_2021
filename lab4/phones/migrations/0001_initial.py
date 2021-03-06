# Generated by Django 4.0 on 2021-12-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('model_name', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=30)),
                ('display_diagonal', models.IntegerField(default=0)),
                ('battery_capacity', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
    ]
