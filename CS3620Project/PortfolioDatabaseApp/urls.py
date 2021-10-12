from . import views
from django.urls import path

app_name = 'PortfolioDatabaseApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('Contact/', views.Contact, name="Contact"),
    path('Hobbies/', views.Hobbies, name="Hobbies"),
    path("<int:Hobbies_id>", views.HobbiesDescriptionDetail, name="HobbiesDescriptionDetail"),
    path('Home/', views.Home, name="Home"),
    path('MyPortfolio/', views.MyPortfolio, name="MyPortfolio"),
    path("<int:MyPortfolio_id>", views.MyPortfolioDetailed, name="MyPortfolioDetailed"),
]