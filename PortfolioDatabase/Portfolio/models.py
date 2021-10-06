from django.db import models


# Create your models here.

class Portfolio(models.Model):

    def __str__(self):
        PName_PDescription = self.Portfolio_Name + "<br>" + self.Portfolio_Description + "<br>" + "<br>"
        return PName_PDescription

    Portfolio_Name = models.CharField(max_length=200)
    Portfolio_Description = models.CharField(max_length=200)