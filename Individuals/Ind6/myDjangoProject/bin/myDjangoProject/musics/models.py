from django.db import models

# Create your models here.

class Meta:
	db_table = 'musics'

class Country(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100, verbose_name = 'название ')
	population = models.IntegerField(default = 0, verbose_name = 'население ')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Musician(models.Model):
	id = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length = 100, verbose_name = 'имя ')
	second_name = models.CharField(max_length = 100, verbose_name = 'фамилия ')
	dateOfBirth = models.DateField(verbose_name = 'дата рождения')

	def __unicode__(self):
		return self.first_name + " " + self.second_name

	def __str__(self):
		return self.first_name + " " + self.second_name

class MusicStyle(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100, verbose_name = 'Название направления')
	country = models.ForeignKey('Country',null = True, blank = True, verbose_name = 'Зародилась в ')
	description = models.TextField(verbose_name = 'Описание')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class Music(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100, verbose_name = 'Название ')
	musician = models.ForeignKey('Musician',null = True, blank = True, verbose_name = 'Автор ')
	musicStyle = models.ForeignKey('MusicStyle',null = True, blank = True, verbose_name = 'Стиль ')
	description = models.TextField(verbose_name = 'Описание')
	timestamp = models.DateTimeField(verbose_name = 'Время создания', auto_now = True)
	updated = models.DateTimeField(verbose_name = 'Время обновления', auto_now = True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
