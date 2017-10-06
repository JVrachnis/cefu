from django import forms
from .models import SingUp
class SingUpForm(forms.ModelForm):
	class Meta:
		password =forms.CharField(widget=forms.PasswordInput)
		model=SingUp
		fields = '__all__'
		widgets = {
			'password' : forms.PasswordInput(),
		}
