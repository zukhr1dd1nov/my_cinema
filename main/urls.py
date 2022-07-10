from django.urls import path
from main.views import Main

urlpatterns = [
    path('',Main.as_view(),name='home')
]