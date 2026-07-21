from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    image = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name