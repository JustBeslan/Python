from django import forms
from .models import Music, Musician, MusicStyle, Country

class MusicForm(forms.ModelForm):
	model = forms.Form
	class Meta:
		model = Music
		fields = ['name','musician','musicStyle','description']

class MusicianForm(forms.ModelForm):
	model = forms.Form
	class Meta:
		model = Musician
		fields = ['first_name','second_name','dateOfBirth']

class MusicStyleForm(forms.ModelForm):
	model = forms.Form
	class Meta:
		model = MusicStyle
		fields = ['name','country','description']

class CountryForm(forms.ModelForm):
	model = forms.Form
	class Meta:
		model = Country
		fields = ['name','population']
