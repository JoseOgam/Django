from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    datestamp = models.DateTimeField(auto_now_add=True)
