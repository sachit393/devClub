from django import forms
from .models import User,Request
class ModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model=User
        fields= "__all__"

class BorrowForm(forms.ModelForm):
    class Meta:
        model=Request
        fields='__all__'



