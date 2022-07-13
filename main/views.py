import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Create your views here.
from main.forms import ContactModelForm
from main.models import MovieModel, CategoryModel, ScheduleModel , BRANCHES


class HomeView(ListView):
    template_name = 'main/index.html'
    queryset = MovieModel.objects.filter(is_active=True,is_part_of_banner=True)
    context_object_name = 'banners'
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['choices'] = MovieModel.objects.filter(is_active=True)
        date = self.request.GET.get('date')
        movie = self.request.GET.get('movie')
        if date == '' and movie != 'None':
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(),movie__is_active=True,movie_id=movie).order_by('date','time')
        elif date != '' and date is not None and movie == 'None':
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(),movie__is_active=True,date=datetime.datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d')).order_by('date','time')
        elif date != '' and date is not None and movie != 'None':
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(),movie__is_active=True,movie_id=movie,date=datetime.datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d')).order_by('date','time')
        return data

class AboutView(TemplateView):
    template_name = 'main/about.html'

class ScheduleView(ListView):
    template_name = 'main/schedule.html'
    model = ScheduleModel

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['is_searched']=False
        data['choices'] = MovieModel.objects.filter(is_active=True)
        date = self.request.GET.get('date')
        movie = self.request.GET.get('movie')
        if date == '' and movie != 'None':
            data['is_searched'] = True
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(), movie__is_active=True,movie_id=movie).order_by('date', 'time')
        elif date != '' and date is not None and movie == 'None':
            data['is_searched'] = True
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(), movie__is_active=True,date=datetime.datetime.strptime(self.request.GET.get('date'),'%Y-%m-%d')).order_by('date','time')
        elif date != '' and date is not None and movie != 'None':
            data['is_searched'] = True
            data['date'] = ScheduleModel.objects.filter(date__gte=datetime.datetime.today(), movie__is_active=True,movie_id=movie,date=datetime.datetime.strptime(self.request.GET.get('date'),'%Y-%m-%d')).order_by('date','time')
        return data


class MoviesView(ListView):
    template_name = 'main/movies.html'
    model = CategoryModel

class MovieDetailView(DetailView):
    template_name = 'main/movie_detail.html'
    model = MovieModel


class ContactsView(CreateView):
    template_name = 'main/contacts.html'
    form_class = ContactModelForm
    model = CategoryModel

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['branches'] = BRANCHES
        return data

    def post(self, request, *args, **kwargs):
        form = ContactModelForm(data=self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'main/contacts.html',{'form':form})