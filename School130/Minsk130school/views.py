import os
from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from .forms import AdmissionApplicationForm, QuestionsForm, DisplayForm
from django.contrib import messages
import zipfile
from django.views import View

# Create your views here.

def home (request):
    application_form = AdmissionApplicationForm()
    question_form = QuestionsForm()
    blogs = models.Blogs.objects.order_by('-publicationDate')
    teachers = models.Teachers.objects.all()
    courses = models.PaidServices.objects.all()
    admins = models.LeadershipContacts.objects.all()
    for course in courses:
        course.teachers_set = course.teachers.all()  # Получение всех преподавателей для каждого кружка
    return render(request, 'home.html', {'application_form':application_form,
                                         'question_form':question_form,
                                         'courses': courses,
                                         'teachers':teachers,
                                         'blogs':blogs,
                                         'admins':admins})

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
    
def show_administration (request, admin_id):
    try:
        admin = models.LeadershipContacts.objects.get(id= admin_id) 
    except:
        return HttpResponseNotFound()
    question_form = QuestionsForm() 
    return render(request, 'administration.html', {'admin':admin,
                                            'question_form':question_form})


def show_awards_licenses(request):
    data = [] 
    display_option = 'awards'
    question_form = QuestionsForm()
    display_form = DisplayForm()
    if request.method == 'POST':
        display_option = request.POST.get('display_option')            
        print(display_option)
            
        if display_option == 'awards':
            data = models.Awards.objects.all()
        elif display_option == 'licenses':
            data = models.Licenses.objects.all()
    
    # Проверяем, был ли отправлен POST-запрос или это просто загрузка страницы
    # Если это просто загрузка страницы (GET-запрос), отображаем награды
    if not request.method == 'POST':
        data = models.Awards.objects.all()
    
    return render(request, 'awards.html', 
                          {'data': data,
                           'display_form': display_form,
                           'display_option': display_option,
                           'question_form': question_form})    
    

# сохранение информации в бд из форм, при этом прописываю url add_question и add_admission_application
# и добавляю в шаблоне home.html в атрибут action url-адрес, на который будет отправлена форма
def add_admission_application(request):
    if request.method == 'POST':
        application_form  = AdmissionApplicationForm(request.POST, request.FILES)
        if application_form.is_valid():
            application_form.save()
            messages.success(request, 'Заявка успешно отправлена!')
    else:
        application_form  = AdmissionApplicationForm() 
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
        # Получение заявок и вопросов для экспорта
        applications = models.AdmissionApplication.objects.all()
        questions = models.Questions.objects.all()

        # Создание ZIP-архива
        zip_filename = 'export.zip'
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Добавление файлов с заявками
            for application in applications:
                # Создание содержимого файла для каждой заявки
                file_content = f"ФИО родителя: {application.parent_name}\n"
                file_content += f"Телефон родителя: {application.parent_contact}\n"
                file_content += f"ФИО ученика: {application.student_name}\n"
                file_content += f"Класс: {application.student_class}\n"
                file_content += f"Персональные данные ученика: {application.student_personal_data}\n"
                file_content += f"Персональные данные родителя: {application.parent_personal_data}\n"
                zipf.writestr(f'application_{application.id}.txt', file_content)
            
                # Проверка наличия прикрепленного файла и добавление его в архив
                if application.attached_files:
                    file_path = application.attached_files.path    #проверяю наличие прикрепленного файла (attached_files) и добавляю его в архив
                    #с помощью zipf.write().
                    # проверка, существует ли файл на диске (os.path.exists(file_path)), 
                    # чтобы избежать ошибок, если файл был удален или перемещен.
                    
                    if os.path.exists(file_path):
                        zipf.write(file_path, f'application_{application.id}_{application.attached_files.name}')
            
            # Добавление файлов с вопросами
            for question in questions:
                # Создание содержимого файла для каждого вопроса
                file_content = f"Имя: {question.name}\n"
                file_content += f"Email: {question.email}\n"
                file_content += f"Сообщение: {question.message}\n"
                zipf.writestr(f'question_{question.id}.txt', file_content)

        # Возврат архива в HTTP-ответе
        with open(zip_filename, 'rb') as zip_file:
            response = HttpResponse(zip_file.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="export.zip"'
            return response
