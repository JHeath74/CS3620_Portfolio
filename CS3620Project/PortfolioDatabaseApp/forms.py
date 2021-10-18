from django import forms
from .models import Create_Contact, Portfolio


class ContactInformationForm(forms.ModelForm):
    class Meta:

        model = Create_Contact
        fields = ['ContactName', 'ContactEmail', 'ContactMessage']


class PortfolioInformationForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['PortfolioName', 'PortfolioDescription', 'PortfolioImage']