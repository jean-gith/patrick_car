from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label='Nom utilisateur',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Mot de pass',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nom utilisateur',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Mot de pass',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    telephone = forms.CharField(label='Numero de Telephone',widget=forms.NumberInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Mot de pass confirmaion',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    localisation = forms.CharField(label='Localisation Geographique',widget=forms.TextInput(attrs={'class':'form-control'}))
    