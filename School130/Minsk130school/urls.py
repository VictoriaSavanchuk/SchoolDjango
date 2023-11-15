from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('home/news/', views.show_news, name= 'news'),
    path('home/teachers/', views.show_teachers, name= 'teachers'),
    path('home/teachers/<int:teacher_id>/', views.show_teacher, name= 'teacher'),
        
]