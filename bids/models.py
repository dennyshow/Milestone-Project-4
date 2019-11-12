from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_no = models.IntegerField()
    bid_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    
    def __str__(self):
        return str(self.user_id)