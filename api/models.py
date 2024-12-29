from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name
    
    
class Watchlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
