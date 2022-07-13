from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import MovieModel, ScheduleModel, CategoryModel, ContactModel


# Register your models here.

def activate(modeladmin, request, queryset):
    queryset.update(is_active=True)
def deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)

def is_banner(modeladmin, request, queryset):
    queryset.update(is_part_of_banner=True)
def not_banner(modeladmin, request, queryset):
    queryset.update(is_part_of_banner=False)

is_banner.short_description = 'Сделать частью баннера'
not_banner.short_description = 'Убрать из части баннера'
deactivate.short_description = 'Сделать неактивным'
activate.short_description = 'Сделать активным'

@admin.register(ScheduleModel)
class ScheduleModelAdmin(admin.ModelAdmin):
     list_display = ['id','date','time']

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
     list_display = ['id','name','last_name','where','created_at']

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
    list_display = ['id','title','created_at','is_active','is_part_of_banner']
    actions = [activate,deactivate,is_banner,not_banner]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }