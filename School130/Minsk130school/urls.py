from django.urls import path
from . import views


urlpatterns = [
    path('home/add_admission_application/', views.add_admission_application, name='add_admission_application'),
    path('home/add_question/', views.add_question, name='add_question'),
    path('home/', views.home, name= 'home'),
    path('home/news/', views.show_news, name= 'news'),
    path('home/teachers/', views.show_teachers, name= 'teachers'),
    path('home/teachers/<int:teacher_id>/', views.show_teacher, name= 'teacher'),
    path('export/', views.ExportView.as_view(), name='export'),  
]