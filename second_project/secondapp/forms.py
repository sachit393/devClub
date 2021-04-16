from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("SHOULD SHART WITH Z")

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verify_email=forms.EmailField(label='reenter email')
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])

    #clean data for entire form
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if(email!=vmail):
            raise forms.ValidationError('emails do not match')

# custom validators using validators class
#self made validator function based
    # def clean_botcatcher(self):
    #
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('GOTCHA')
    #     return botcatcher