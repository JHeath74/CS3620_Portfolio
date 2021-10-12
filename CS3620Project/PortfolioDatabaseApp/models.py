from django.db import models


# Create your models here.
class Hobby(models.Model):

    def __str__(self):
        return self.HobbyName

    HobbyName = models.CharField(max_length=200)
    HobbyDescription = models.CharField(max_length=200)
    HobbyImage = models.CharField(max_length=500, default="https://media.istockphoto.com/vectors/outline-colorful-doodle-hobbies-set-stay-home-concept-top-table-and-vector-id1222703360?s=612x612")


class Portfolio(models.Model):

    def __str__(self):
        return self.PortfolioName

    PortfolioName = models.CharField(max_length=200)
    PortfolioDescription = models.CharField(max_length=200)
    PortfolioImage = models.CharField(max_length=500, default="https://centralaz.edu/wp-content/uploads/2017/08/CIS_Comp_Prog_Main_507378942.jpg")
