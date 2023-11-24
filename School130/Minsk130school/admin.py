from django.contrib import admin
from .models import *
from django.urls import reverse
from django.urls import path
from . import views
# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'publicationDate', 'image_tag')  
    list_display_links = ('id', 'title', 'content', 'publicationDate', 'image_tag')
    list_filter = ('id', 'publicationDate')
    ordering = ['publicationDate']

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'brief_information', 'description', 'paid_service', 'image_tag')  
    list_display_links = ('first_name', 'last_name', 'description', 'paid_service', 'image_tag')
    ordering = ['last_name', 'first_name']

    
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')
    list_display_links = ('title', 'description', 'image_tag')
    
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file')
    list_display_links = ('title', 'description', 'file')
    
class LicensesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag')  
    list_display_links = ('title', 'description', 'image_tag') 
    
class LeadershipContactsAdmin(admin.ModelAdmin):
    list_display = ('position', 'first_name', 'last_name', 'contact_info', 'image_tag')  
    list_display_links = ('position', 'first_name', 'last_name', 'contact_info', 'image_tag')  
    ordering = ['position']
    
class AdmissionApplicationAdmin(admin.ModelAdmin):
    def export_link(self, obj):
        # Генерация ссылки на экспорт для каждого объекта
        export_url = reverse('export')  #  URL-шаблон для представления экспорта
        return format_html('<a href="{}">Export</a>', export_url)

    export_link.short_description = "Выгрузить файлы" 
    
    list_display = ('student_class', 'parent_name', 'parent_contact', 'student_name', 'student_personal_data', 'parent_personal_data', 'attached_files', 'export_link')  
    list_display_links =  ('student_class', 'parent_name', 'parent_contact', 'student_name', 'student_personal_data', 'parent_personal_data', 'attached_files')  

class PaidServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_tag', 'category') 
    list_display_links = ('title', 'description', 'image_tag', 'category') 
    
class QuestionsAdmin(admin.ModelAdmin):
    def export_link(self, obj):
        # Генерация ссылки на экспорт для каждого объекта
        export_url = reverse('export')  #  URL-шаблон для представления экспорта
        return format_html('<a href="{}">Export</a>', export_url)

    export_link.short_description = "Выгрузить файлы"  # Название столбца в административной панели
    
    list_display = ('name', 'email', 'message', 'export_link') 
    list_display_links = ('name', 'email', 'message') 
    
#Файловый менеджер
class FileAdmin(admin.ModelAdmin):
    def file_list(self, obj):
        file_list_url = reverse('file_list')  #  URL-шаблон для представления экспорта
        return format_html('<a href="{}">Просмотр</a>', file_list_url)

    file_list.short_description = "Просмотр файлов"
    list_display = ('name', 'file_path', 'created_date', 'file_list')
    
    def get_urls(self):
        # Регистрируем URL-маршруты для админки
        urls = super().get_urls()
        my_urls = [
            path('files/', self.admin_site.admin_view(views.FileListView.as_view()), name='admin_file_list'),
            path('upload/', self.admin_site.admin_view(views.UploadFileView.as_view()), name='admin_upload_file'),
            path('create_folder/', self.admin_site.admin_view(views.CreateFolderView.as_view()), name='admin_create_folder'),
        ]
        return my_urls + urls
    
    def get_changeform_initial_data(self, request):
        return {'_redirect': reverse('admin_file_list')}
            
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Awards, AwardsAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Licenses, LicensesAdmin)
admin.site.register(LeadershipContacts, LeadershipContactsAdmin)
admin.site.register(AdmissionApplication, AdmissionApplicationAdmin)
admin.site.register(CategoriesPaidServices)
admin.site.register(PaidServices, PaidServicesAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(File, FileAdmin)