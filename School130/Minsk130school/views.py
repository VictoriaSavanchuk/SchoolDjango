from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from .forms import AdmissionApplicationForm, QuestionsForm
from django.contrib import messages
import csv
from django.views import View

# Create your views here.

def home (request):
    application_form = AdmissionApplicationForm()
    question_form = QuestionsForm()
    blogs = models.Blogs.objects.order_by('-publicationDate')
    teachers = models.Teachers.objects.all()
    courses = models.PaidServices.objects.all()
    for course in courses:
        course.teachers_set = course.teachers.all()  # Получение всех преподавателей для каждого кружка
    return render(request, 'home.html', {'application_form':application_form,
                                         'question_form':question_form,
                                         'courses': courses,
                                         'teachers':teachers,
                                         'blogs':blogs})

def show_news (request):
    blogs = models.Blogs.objects.order_by('-publicationDate')
    print(f'blogs = {blogs}')     
    paginator = Paginator(blogs, 4)   #показ на стр. по 4 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    question_form = QuestionsForm()
    return render(request, 'news.html', {'info': page_obj,
                                         'question_form':question_form})

def show_teachers (request):
    teachers = models.Teachers.objects.all()    
    paginator = Paginator(teachers, 4)   
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    question_form = QuestionsForm()
    return render(request, 'teachers.html', {'info': page_obj,
                                             'question_form':question_form})

def show_teacher (request, teacher_id):
    try:
        teacher = models.Teachers.objects.get(id= teacher_id) 
    except:
        return HttpResponseNotFound()
    question_form = QuestionsForm() 
    return render(request, 'teacher.html', {'teacher':teacher,
                                            'question_form':question_form})

# сохранение информации в бд из форм, при этом прописываю url add_question и add_admission_application
# и добавляю в шаблоне home.html в атрибут action url-адрес, на который будет отправлена форма
def add_admission_application(request):
    if request.method == 'POST':
        application_form  = AdmissionApplicationForm(request.POST, request.FILES)
        if application_form.is_valid():
            application_form.save()
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('home')   # Перенаправляем пользователя на главную страницу после успешного сохранения формы
    

def add_question(request):
    if request.method == 'POST':
        question_form = QuestionsForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('home')
        
    


class ExportView(View):
    def get(self, request):
        # Получение вопросов и заявок для экспорта
        questions = models.Questions.objects.all()
        materials = models.AdmissionApplication.objects.all()

        # Создаю CSV-файл
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        # Открытие файла CSV с указанием кодировки
        writer_materials = csv.writer(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, encoding='utf-8')
        writer_materials.writerow(['ФИО родителя', 'Телефон родителя', 'ФИО ученика', 'Класс', 'Персональные данные ученика', 'Персональные данные родителя', 'Прикрепленные файлы'])  # Заголовки столбцов

        writer_question = csv.writer(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, encoding='utf-8')
        writer_question.writerow(['Имя', 'Email', 'Сообщение'])
        
        # Запись вопросов в CSV
        for question in questions:
            writer_question.writerow([question.name, question.email, question.message])

        # Запись заявок в CSV
        for material in materials:
            writer_materials.writerow([material.parent_name, material.parent_contact, 
                                       material.student_name, material.student_class, material.student_personal_data,
                                       material.parent_personal_data, material.attached_files])

        return response
