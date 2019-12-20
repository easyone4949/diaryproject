from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
