from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hobby, Portfolio
from django.template import loader


# Create your views here.

def index(request):
    return HttpResponse()


def Contact(request):
    template = loader.get_template("PortfolioDatabaseApp/Contact.html")
    return HttpResponse(template.render())


def Hobbies(request):
    HobbyList = Hobby.objects.all()
    context = {
        "HobbyList": HobbyList,

    }
    return render(request, "PortfolioDatabaseApp/Hobbies.html", context)


def HobbiesDescriptionDetail(request, Hobbies_id):
    hobbiesdescription = Hobby.objects.get(pk=Hobbies_id)
    context = {
        "hobbiesdescription": hobbiesdescription
    }
    return render(request, "PortfolioDatabaseApp/HobbiesDescriptionDetail.html", context)


def Home(request):
    template = loader.get_template("PortfolioDatabaseApp/Home.html")
    return HttpResponse(template.render())


def MyPortfolio(request):
    PortfolioList = Portfolio.objects.all()
    context = {
        'PortfolioList': PortfolioList,
    }
    return render(request, "PortfolioDatabaseApp/PortfolioList.html", context)


def MyPortfolioDetailed(request, MyPortfolio_id):
    portfoliodescription = Portfolio.objects.get(pk=MyPortfolio_id)
    context = {
        "portfoliodescription": portfoliodescription
    }
    return render(request, "PortfolioDatabaseApp/MyPortfolioDescriptionDetail.html", context)
