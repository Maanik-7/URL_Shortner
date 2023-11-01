from django.db import models
import shortuuid

# Create your models here.

def generate_default_short_url():
    return f'{shortuuid.ShortUUID().random()}'

class urlshortner(models.Model):
    long_url = models.CharField(max_length=10000)
    short_url = models.CharField(max_length=20)

    def __str__(self):
        return self.short_url




