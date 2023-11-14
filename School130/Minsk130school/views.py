from django.shortcuts import render
from . import models
# Create your views here.

def home (request):
    return render(request, 'base.html', {'home':home})

def slider_view(request):
    courses = models.PaidServices.objects.all()
    return render(request, 'base.html', {'courses': courses})