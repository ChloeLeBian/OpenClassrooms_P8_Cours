from django import forms
from listings.models import User, Ticket, Review
from django.contrib.auth.forms import UserCreationForm


class SubscribeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'password1': forms.PasswordInput(attrs={"class":"form-control"}),
        'password2': forms.PasswordInput(attrs={"class":"form-control"}),
        'username' : forms.TextInput(attrs={"class":"form-control"})
    }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
      
class TicketCreation(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', 'user']

class ReviewCreation(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['ticket', 'rating', 'headline', 'body', 'user']
        