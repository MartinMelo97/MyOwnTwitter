from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class RegisterForm(forms.ModelForm):
	password = forms.CharField(label="password", widget=forms.PasswordInput)
	cpassword = forms.CharField(label="confirm", widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','email']

	def clean_cpassword(self):
		clean_data = self.cleaned_data
		if clean_data['password'] != clean_data['cpassword']:
			raise forms.ValidationError('Contraseñas no coinciden')
		return clean_data['cpassword']

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','email']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['cellphone', 'birth', 'profile_img', 'back_img']