from modeltranslation.translator import translator, TranslationOptions
from .models import MovieModel, CategoryModel


@translator.register(MovieModel)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@translator.register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name')