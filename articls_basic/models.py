from django.db import models

# Create your models here.

class Article(models.Model):
    titel = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)
    auther = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel
