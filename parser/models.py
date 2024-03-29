from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return f'{self.title}, {self.location}'
    
    
