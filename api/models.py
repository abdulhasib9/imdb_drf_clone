from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models  import User





class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=150)
    
    def __str__(self):
        return self.name
    
    
class Watchlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Review(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist = models.ForeignKey(Watchlist,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+ " "+self.watchlist.title