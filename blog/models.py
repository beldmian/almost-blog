from django.db import models

class Articles(models.Model):
    image = models.ImageField(default="https://picsum.photos/200/1000/")
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=20)
