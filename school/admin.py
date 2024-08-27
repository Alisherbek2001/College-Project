from django.contrib import admin
from .models import Slider,About,OurHistory,Result,Partner
from django.utils.translation import gettext_lazy as _

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Image'), {'fields': ('image',)}),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title_uz','title','title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Slug'), {'fields': ('slug', )}),
        (_('Image'), {'fields': ('image',)}),
    )
    
@admin.register(OurHistory)
class OurhistoryAdmin(admin.ModelAdmin):
    list_display = ('history_year',)
    fieldsets = (
        (_("History year"),{'fields':('history_year',)}),
        (_('Uzbek'), {'fields': ('description_uz',)}),
        (_('Russian'), {'fields': ('description_ru',)}),
        (_('English'), {'fields': ('description_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )
    
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets = (
        (_('Uzbek'),{'fields':('name_uz',)}),
        (_('Russian'),{'fields':('name_ru',)}),
        (_('English'),{'fields':('name_en',)}),
        (_('Amount'), {'fields': ('amount',)}),
        (_('Icon'), {'fields': ('icon',)}),
        
    )
    
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name_uz','name_ru','name_en')
    fieldsets =(
        (_('Uzbek'),{'fields':('name_uz',)}),
        (_('Russian'),{'fields':('name_ru',)}),
        (_('English'),{'fields':('name_en',)}),
        (_('Link'), {'fields': ('link',)}),
        (_('Icon'), {'fields': ('icon',)}),
    )