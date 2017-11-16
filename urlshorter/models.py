from django.db import models

class Url(models.Model):
    URL = models.CharField(max_length=256)
    Code = models.CharField(max_length=128)

    def __str__(self):
        return self.URL
