from django.db import models

# Create your models here.


class Hobbies(models.Model):

    def __str__(self):
        return self.Hobby_Name, self.Hobby_Description

    Hobby_Name = models.CharField(max_length=200)
    Hobby_Description = models.CharField(max_length=200)