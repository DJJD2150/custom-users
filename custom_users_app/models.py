from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    url = models.URLField(null=True)
    age = models.IntegerField(blank=True, null=True)
    # According to Joe's demo, 'blank=True' means you can submit an empty bio 
    # and 'null=True' means you can store it in the database.
    homepage = models.CharField(max_length=300)
    bio = models.TextField(blank=True, null=True)
    # This is for the extra credit.
    REQUIRED_FIELDS = ['age']

    def __str__(self):
        return self.username
