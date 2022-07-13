from django.urls import path
from main.views import HomeView, AboutView, MoviesView, MovieDetailView, ScheduleView, ContactsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path('movies/movie/<int:pk>', MovieDetailView.as_view(), name='movie'),
    path('schedule', ScheduleView.as_view(), name='schedule'),
    path('contacts/', ContactsView.as_view(), name='contacts')
]
