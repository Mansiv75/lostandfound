from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    reported_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Lost {self.name} o {self.date} at {self.location} by {self.user.username}"

class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    reported_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Found {self.name} on {self.date} at {self.location} by {self.user.username}"