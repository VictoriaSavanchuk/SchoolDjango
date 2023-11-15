from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator

# Create your views here.

def home (request):
    return render(request, 'home.html', {'home':home})

def show_news (request):
    blogs = models.Blogs.objects.all()    
    print(f'blogs = {blogs}')     
    paginator = Paginator(blogs, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'info': page_obj})

def show_teachers (request):
    teachers = models.Teachers.objects.all()    
    paginator = Paginator(teachers, 4)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'teachers.html', {'info': page_obj})

def show_teacher (request, teacher_id):
    try:
        teacher = models.Teachers.objects.get(id= teacher_id) 
    except:
        return HttpResponseNotFound() 
    return render(request, 'teacher.html', {'teacher':teacher})

# def slider_view(request):
#     print('hi')
#     courses = models.PaidServices.objects.all()
#     print(courses)
#     return render(request, 'news.html', {'courses': courses})