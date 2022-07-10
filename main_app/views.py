from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finches, Toy

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def finches_index(request):
    finches = Finches.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finches_id):
    finches = Finches.objects.get(id=finches_id)
    return render(request, 'finches/detail.html', { 'finches': finches })

class ToysList(ListView):
    model = Toy
    template_name: 'toys/index.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = "toys/detail.html"
    

class FinchesCreate(CreateView):
    model = Finches
    fields = '__all__'
    success_url = '/finches/'

class FinchesUpdate(UpdateView):
    model = Finches
    fields = ['description']

class FinchesDelete(DeleteView):
    model = Finches
    success_url = '/finches/'