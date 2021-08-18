from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='album/')
    description = models.TextField()
    time_since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title