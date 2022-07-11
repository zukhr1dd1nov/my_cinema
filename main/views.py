from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from main.models import MovieModel, CategoryModel


class HomeView(ListView):
    template_name = 'main/index.html'
    queryset = MovieModel.objects.filter(is_active=True,is_part_of_banner=True)
    context_object_name = 'banners'

class AboutView(TemplateView):
    template_name = 'main/about.html'


class MoviesView(ListView):
    template_name = 'main/movies.html'
    model = CategoryModel

class MovieDetailView(DetailView):
    template_name = 'main/movie_detail.html'
    model = MovieModel


class Contacts(TemplateView):
    template_name = 'main/contacts.html'