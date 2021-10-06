from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


# Create your views here.

def MyPortfolio(request):
    portfolioList = Portfolio.objects.all()

    return HttpResponse(portfolioList)
