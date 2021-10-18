from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Hobby, Portfolio, Create_Contact
from django.template import loader
from .forms import ContactInformationForm, PortfolioInformationForm


# Create your views here.

def index(request):
    template = loader.get_template("PortfolioDatabaseApp/Index.html")
    return HttpResponse(template.render())


def contacts(request):
    ContactList = Create_Contact.objects.all()
    context = {
        "ContactList": ContactList,
    }
    return render(request, "PortfolioDatabaseApp/Contact.html", context)


def addcontacts(request):
    form = ContactInformationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("PortfolioDatabaseApp:index")

    return render(request, "PortfolioDatabaseApp/Contact-Form.html", {'form': form})


def hobbies(request):
    HobbyList = Hobby.objects.all()
    context = {
        "HobbyList": HobbyList,

    }
    return render(request, "PortfolioDatabaseApp/Hobbies.html", context)


def hobbiesdescriptiondetail(request, Hobbies_id):
    hobbiesdescription = Hobby.objects.get(pk=Hobbies_id)
    context = {
        "hobbiesdescription": hobbiesdescription
    }
    return render(request, "PortfolioDatabaseApp/HobbiesDescriptionDetail.html", context)


def home(request):
    template = loader.get_template("PortfolioDatabaseApp/Home.html")
    return HttpResponse(template.render())


def myportfolio(request):
    PortfolioList = Portfolio.objects.all()
    context = {
        'PortfolioList': PortfolioList,
    }
    return render(request, "PortfolioDatabaseApp/PortfolioList.html", context)


def add_portfolio_item(request):
    form = PortfolioInformationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("PortfolioDatabaseApp:index")

    return render(request, "PortfolioDatabaseApp/Portfolio-Form.html", {'form': form})


def update_portfolio_item(request, id):
    portfolioupdate = Portfolio.objects.get(id=id)
    form = PortfolioInformationForm(request.POST or None, instance=portfolioupdate)
    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabaseApp:index')

    return render(request, 'PortfolioDatabaseApp/Portfolio-Form.html',
                  {'form': form, 'portfolioupdate': portfolioupdate})


def delete_portfolio_item(request, id):
    portfoliodelete = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        portfoliodelete.delete()
        return redirect('PortfolioDatabaseApp:index')

    return render(request, 'PortfolioDatabaseApp/portfoliodelete.html', {'portfoliodelete': portfoliodelete})


def myportfoliodetailed(request, myportfolio_id):
    portfoliodescription = Portfolio.objects.get(pk=myportfolio_id)
    context = {
        "portfoliodescription": portfoliodescription
    }
    return render(request, "PortfolioDatabaseApp/MyPortfolioDescriptionDetail.html", context)
