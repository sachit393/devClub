from django import forms
from django.core import validators



class FormName(forms.Form):
    name=forms.CharField(max_length=264)
    email=forms.CharField(max_length=264)

    #clean data for entire form

# custom validators using validators class
#self made validator function based
    # def clean_botcatcher(self):
    #
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('GOTCHA')
    #     return botcatcher