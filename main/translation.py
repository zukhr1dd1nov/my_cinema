from modeltranslation.translator import translator, TranslationOptions
from .models import MovieModel, CategoryModel

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

translator.register(MovieModel,MovieTranslationOptions)
translator.register(CategoryModel,CategoryTranslationOptions)