from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phone(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING)
    diag = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.model
