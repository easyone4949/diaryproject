from django.db import models

# Create your models here.
class Zimon(models.Model):
    title = models.CharField(max_length= 100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:90]

class Mum(models.Model):
    title = models.CharField(max_length= 100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:90]