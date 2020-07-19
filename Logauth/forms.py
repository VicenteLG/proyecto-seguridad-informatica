from django import forms

CARGO = (
	('XX', 'INSERTAR CARGO'),
	('XX', 'INSERTAR CARGO'),
)

DEPARTAMENTO = (
	('XX', 'INSERTAR DEPARTAMENTO'),
	('XX', 'INSERTAR DEPARTAMENTO'),
)

SUCURSAL = (
	('SA', 'Santiago'),
	('PR', 'Providencia'),
)

class ProfileForm(forms.Form):
	username = forms.CharField(label='Usuario', max_length=100)
	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=100)
	primer_nombre = forms.CharField(label='Primero Nombre', max_length=25)
	segundo_nombre = forms.CharField(label='Segundo Nombre', max_length=25)
	apellido_paterno = forms.CharField(label='Apellido Paterno', max_length=25)
	apellido_materno = forms.CharField(label='Apellido Materno', max_length=25)
	age = forms.IntegerField(label='Edad', min_value=1)
	email = forms.EmailField(label='Email')
	rut = forms.CharField(label='Rut', max_length=12)
	cargo = forms.ChoiceField(label='Cargo', widget=forms.Select, choices=CARGO)
	departamento = forms.ChoiceField(label='Departamento', widget=forms.Select, choices=DEPARTAMENTO)
	sucursal = forms.ChoiceField(label='Sucursal', widget=forms.Select, choices=SUCURSAL)