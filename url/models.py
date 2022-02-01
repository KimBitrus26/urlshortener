from django.db import models

# Create your models here.

class ShortenURL(models.Model):
    original_url = models.URLField(max_length=700)
    shorten_url = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.original_url}"