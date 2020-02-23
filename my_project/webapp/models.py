from django.db import models

# Create your models here.

class Template(models.Model):
    template_name = models.CharField(max_length=100)
    delimeter = models.CharField(max_length=100)
    encode = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    sub_catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.template_name
