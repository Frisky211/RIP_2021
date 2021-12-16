from django.db import models

class Phone(models.Model):
    manufacturer = models.CharField(max_length=50)
    release_date = models.DateField()
    model_name = models.CharField(max_length=50)
    os = models.CharField(max_length=30)
    display_diagonal = models.IntegerField(default=0)
    battery_capacity = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return self.model_name
