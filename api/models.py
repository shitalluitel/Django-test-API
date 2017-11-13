from django.db import models
from users.models import User


# Create your models here.

class Api(models.Model):
    user = models.ForeignKey(User, related_name="api", on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()

