from django.urls import path
from main.views import HomeView, AboutView, MoviesView, MovieDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/movie/<int:pk>', MovieDetailView.as_view(), name='movie')
]
