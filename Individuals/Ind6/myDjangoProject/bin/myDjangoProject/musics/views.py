from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Country, Musician, MusicStyle, Music
from .forms import *
# Create your views here.


def list_all(request):
	MusicSet = Music.objects.all()
	MusicianSet = Musician.objects.all()
	CountrySet = Country.objects.all()
	MusicStyleSet = MusicStyle.objects.all()
	context = {
		'MusicSet' : MusicSet,
		'MusicianSet' : MusicianSet,
		'CountrySet' : CountrySet,
		'MusicStyleSet' : MusicStyleSet
	}
	return render(request,'index.html',context)

#=======================================Detail=====================================
def music_detail(request, id = None):
	instance = get_object_or_404(Music,id = id)
	context = {
		'title' : instance.name,
		'instance' : instance
	}
	return render(request,'music_detail.html',context)

def musician_detail(request, id = None):
	instance = get_object_or_404(Musician,id = id)
	context = {
		'title' : instance.first_name + ' ' + instance.second_name,
		'instance' : instance
	}
	return render(request,'musician_detail.html',context)

def musicStyle_detail(request, id = None):
	instance = get_object_or_404(MusicStyle,id = id)
	context = {
		'title' : instance.name,
		'instance' : instance
	}
	return render(request,'musicStyle_detail.html',context)

def country_detail(request, id = None):
	instance = get_object_or_404(Country,id = id)
	context = {
		'title' : instance.name,
		'instance' : instance
	}
	return render(request,'country_detail.html',context)
#=============================================Create===============================
def music_create(request):
	form = MusicForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'function' : 'Создать',
		'title':'Create Music',
		'form':form
		}
	return render(request,'create.html',context)

def musician_create(request):
	form = MusicianForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'function' : 'Создать',
		'title':'Create Musician',
		'form':form
		}
	return render(request,'create.html',context)

def country_create(request):
	form = CountryForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'function' : 'Создать',
		'title':'Create Country',
		'form':form
		}
	return render(request,'create.html',context)

def musicStyle_create(request):
	form = MusicStyleForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'function' : 'Создать',
		'title':'Create MusicStyle',
		'form':form
		}
	return render(request,'create.html',context)
#=========================================Update==================================
def music_update(request,id=None):
	instance = get_object_or_404(Music,id=id)
	form = MusicForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'function':'Сохранить',
		'title':instance.name,
		'instance':instance,
		'form':form
	}

	return render(request,'create.html',context)

def musician_update(request,id=None):
	instance = get_object_or_404(Musician,id=id)
	form = MusicianForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'function':'Сохранить',
		'title':instance.first_name + ' ' + instance.second_name,
		'instance':instance,
		'form':form
	}

	return render(request,'create.html',context)

def country_update(request,id=None):
	instance = get_object_or_404(Country,id=id)
	form = CountryForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'function':'Сохранить',
		'title':instance.name,
		'instance':instance,
		'form':form
	}

	return render(request,'create.html',context)

def musicStyle_update(request,id=None):
	instance = get_object_or_404(MusicStyle,id=id)
	form = MusicStyleForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		'function':'Сохранить',
		'title':instance.name,
		'instance':instance,
		'form':form
	}

	return render(request,'create.html',context)
#=========================================Delete=======================================
def music_delete(request,id=None):
	music = Music.objects.get(id=id)
	music.delete()
	return HttpResponseRedirect("/")

def musician_delete(request,id=None):
	musician = Musician.objects.get(id=id)
	musician.delete()
	return HttpResponseRedirect("/")

def country_delete(request,id=None):
	country = Country.objects.get(id=id)
	country.delete()
	return HttpResponseRedirect("/")

def musicStyle_delete(request,id=None):
	musicStyle = MusicStyle.objects.get(id=id)
	musicStyle.delete()
	return HttpResponseRedirect("/")
