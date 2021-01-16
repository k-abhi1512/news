from django.db import models

# Create your models here.

# Only model for inserting news by admin
class InsertPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title