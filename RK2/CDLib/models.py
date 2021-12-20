from django.db import models
from django.urls import reverse

class CD(models.Model):
    """
    Модель CD
    """
    name = models.CharField(max_length=50, default='')
    capacity = models.IntegerField(default=100)
    lib = models.ForeignKey('Lib', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CDLib:detail', args=[str(self.id)])

class Lib(models.Model):
    """
    Модель библиотеки
    """
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CDLib:report')
