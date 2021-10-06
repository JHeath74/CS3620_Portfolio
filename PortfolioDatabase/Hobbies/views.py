from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbys


# Create your views here.

def Hobby(request):

    hobbylist = Hobbys.objects.all()
    return HttpResponse(hobbylist)
