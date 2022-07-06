from django.shortcuts import render
from .models import Finches

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def finches_index(request):
    finches = Finches.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })