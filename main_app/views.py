from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Finches

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

class FinchesCreate(CreateView):
    model = Finches
    fields = '__all__'