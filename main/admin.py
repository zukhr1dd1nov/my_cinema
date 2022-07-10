from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import MovieModel, ScheduleModel, CategoryModel


# Register your models here.

@admin.register(ScheduleModel)
class ScheduleModelAdmin(admin.ModelAdmin):
     list_display = ['id','date','time']


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ['id','name']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(MovieModel)
class MovieModelAdmin(TranslationAdmin):
    list_display = ['id','title','created_at','is_active']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }