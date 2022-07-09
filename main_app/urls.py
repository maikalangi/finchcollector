from django.urls import path
from django.views.generic.edit import CreateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finches_id>/', views.finches_detail, name='detail'),
    path('finches/create', views.FinchesCreate.as_view(), name="finches_create"),
]