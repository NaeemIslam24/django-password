from django.db import models

# Create your models here.

class StorePass(models.Model):

    user = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=30,blank=True, null=True)
    gmail = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user) +' '+ self.website
