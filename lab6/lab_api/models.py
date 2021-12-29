from django.db import models


class Manufacturer(models.Model):
    idmanufacturer = models.AutoField(db_column='idManufacturer', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    country = models.CharField(max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'manufacturer'


class Phone(models.Model):
    idphone = models.AutoField(db_column='idPhone', primary_key=True)  # Field name made lowercase.
    model = models.CharField(max_length=45)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturer')  # Field name made lowercase.
    diag = models.IntegerField()
    capacity = models.IntegerField()
    description = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.model

    class Meta:
        managed = True
        db_table = 'phone'
