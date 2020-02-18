from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.IntegerField()
    mark = models.IntegerField()
    division = models.CharField(max_length=50)
    addrs = models.CharField(max_length=50)

    def __str__(self):
        return self.name
