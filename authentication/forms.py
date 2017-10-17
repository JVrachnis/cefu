from django import forms
from .models import User
class UserForm(forms.ModelForm):
        password =forms.CharField(widget=forms.PasswordInput)
        repeatpassword = forms.CharField(widget=forms.PasswordInput)
        class Meta:
                model=User
                fields = ('username','password', 'repeatpassword','email','birthday')
                widgets = {
                        'password' : forms.PasswordInput(),
                	'repeatpassword' : forms.PasswordInput(),
		}

