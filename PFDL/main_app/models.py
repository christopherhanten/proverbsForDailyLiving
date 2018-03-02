from django.db import models

class Proverbs(models.Model):
    date = models.CharField(max_length=12)
    proverb = models.CharField(max_length=2000)

    def __str__(self):
	       return self.proverb

# Create your models here.
