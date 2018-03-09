from django.db import models
from django.contrib.auth.models import User

class Proverb(models.Model):
    date = models.CharField(max_length=10)
    proverb = models.CharField(max_length=2000)
    # user = models.ForeignKey(User,
    # models.SET_NULL,
    # blank=True,
    # null=True,)

def __str__(self):
	    return self.proverb
