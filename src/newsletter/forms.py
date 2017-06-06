from django import forms
from .models import SignUp

class SignUpModelForm(forms.ModelForm):

	class Meta:
		"""
		"""
		model = SignUp
		fields = [ 'full_name', 'email']

	def clean_email(self):
		"""
		"""
		email = self.cleaned_data.get('email')
		base, provider = email.split('@')
		domain, extenstion = provider.split('.')
		# if not domain == 'cisco':
		# 	raise forms.ValidationError('Please use your cisco email id')
		if not extenstion == 'org':
			raise forms.ValidationError("Give proper cisco email id")

		return 'abc@gmail.com'

class ContactForm(forms.Form):
	
	email = forms.EmailField()
	full_name = forms.CharField(required=False)
	message = forms.CharField()

	def clean_email(self):
		"""
		"""
		email = self.cleaned_data.get('email')
		base, provider = email.split('@')
		domain, extenstion = provider.split('.')
		if not extenstion == 'org':
			raise forms.ValidationError('Give proper cisco email id')