from django.db import models
from django.urls import reverse
# Create your models here.

class Model(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200)
    UserName = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.FirstName
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])