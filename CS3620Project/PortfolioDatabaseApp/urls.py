from . import views
from django.urls import path

app_name = 'PortfolioDatabaseApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('Contacts/', views.contacts, name="contacts"),
    path('Hobbies/', views.hobbies, name="Hobbies"),
    path("<int:Hobbies_id>", views.hobbiesdescriptiondetail, name="HobbiesDescriptionDetail"),
    path('Home/', views.home, name="Home"),
    path('MyPortfolio/', views.myportfolio, name="MyPortfolio"),
    path("<int:MyPortfolio_id>", views.myportfoliodetailed, name="MyPortfolioDetailed"),
    path('AddContacts', views.addcontacts, name="addcontacts"),
    path('addportfolio', views.add_portfolio_item, name="add_portfolio_item"),
    path('updateportfolio/<int:id>', views.update_portfolio_item, name="update_portfolio_item"),
    path('deleteportfolio/<int:id>', views.delete_portfolio_item, name="delete_portfolio_item"),

]