from django.contrib import admin
from .models import Country, Musician, MusicStyle, Music

# Register your models here.

class CountryModelAdmin(admin.ModelAdmin):
	list_display = ['name','population']
	list_display_links = ['name','population']
	list_filter = ['name']
	class Meta:
		model = Country

class MusicianModelAdmin(admin.ModelAdmin):
	list_display = ['first_name','second_name','dateOfBirth']
	list_display_links = ['first_name','second_name','dateOfBirth']
	list_filter = ['first_name','second_name','dateOfBirth']
	class Meta:
		model = Musician

class MusicStyleModelAdmin(admin.ModelAdmin):
	list_display = ['name','country','description']
	list_display_links = ['name','country']
	list_filter = ['name','country']
	class Meta:
		model = MusicStyle

class MusicModelAdmin(admin.ModelAdmin):
	list_display = ['name','musician','musicStyle','description', 'timestamp', 'updated']
	list_display_links = ['name','musician','musicStyle']
	list_filter = ['name','musician','musicStyle']
	class Meta:
		model = Music

admin.site.register(Country,CountryModelAdmin)
admin.site.register(Musician,MusicianModelAdmin)
admin.site.register(MusicStyle,MusicStyleModelAdmin)
admin.site.register(Music,MusicModelAdmin)
