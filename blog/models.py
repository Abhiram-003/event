from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Favourites(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="fav_movies")
    mv_id=models.IntegerField(null=True)
    mv_name=models.CharField(max_length=200, null=True)
    mv_poster=models.URLField(null=True)
    mv_over=models.CharField(max_length=500, null=True)
    mv_rating=models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.user.username} likes {self.mv_name}"
