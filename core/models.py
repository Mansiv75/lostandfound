from django.db import models

# Create your models here.
class LostItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    reported_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Lost {self.name} o {self.date} at {self.location}"

class FoundItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    reported_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Found {self.name} on {self.date} at {self.location}"