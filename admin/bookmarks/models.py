from django.db import models
from django.contrib.auth.models import User
class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
