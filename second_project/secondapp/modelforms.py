from django import forms
from .models import User,Request,RenewalRequests
class ModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model=User
        fields= "__all__"

class BorrowForm(forms.ModelForm):
    accept=forms.BooleanField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model=Request
        fields='__all__'

class RenewForm(forms.ModelForm):
    accept=forms.BooleanField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model=RenewalRequests
        fields= ['name','book','renewal_time','accept']

