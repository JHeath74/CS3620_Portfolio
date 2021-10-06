from django.db import models

# Create your models here.

class Hobbys(models.Model):

    def __str__(self):
        Name_Description = self.Hobby_Name + "<br>" + self.Hobby_Description + "<br>" + "<br>"
        return Name_Description

    Hobby_Name = models.CharField(max_length=200)
    Hobby_Description = models.CharField(max_length=200)
