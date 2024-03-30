from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, blank=True)
    href = models.URLField()

    def __str__(self):
        return f'{self.title}, {self.location}'


class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return f'{self.name}, {self.slug}, {self.id}'

    
    
