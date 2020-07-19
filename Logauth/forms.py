from django import forms

class ProfileForm(forms.Form):
	username = forms.CharField(label='Usuario', max_length=100)
	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=100)
	age = forms.IntegerField(label='Edad', min_value=1)
	email = forms.EmailField(label='Email')
	rut = forms.CharField(label='Rut', max_length=12)