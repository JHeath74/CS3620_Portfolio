from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Contact(request):

    return render(request, "Contact.html")
