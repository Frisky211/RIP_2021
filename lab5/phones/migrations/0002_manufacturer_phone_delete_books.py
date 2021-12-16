# Generated by Django 4.0 on 2021-12-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('idmanufacturer', models.AutoField(db_column='idManufacturer', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('idphone', models.AutoField(db_column='idPhone', primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=45)),
                ('diag', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'phone',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
