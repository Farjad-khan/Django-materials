from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="pictures/", default="")
    title = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return self.title
    