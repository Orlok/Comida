from django import forms

class LoginForms(forms.Form):
	usuario = forms.CharField()
	contrasena = forms.CharField(widget=forms.PasswordInput())
	