from django.db import models
from django.utils.html import format_html
from PIL import Image

# Create your models here.

class Blogs(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Содержание')
    publicationDate = models.DateField('Дата публикации', blank=True)
    image = models.ImageField('Изображение', upload_to='blog_images/')
    
    def save(self, *args, **kwargs):   
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        
class Teachers(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    brief_information = models.TextField('Краткая информация') 
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='teacher_images/')
    paid_service = models.ForeignKey('PaidServices',  on_delete=models.SET_DEFAULT, related_name='teachers', verbose_name='Платные услуги',  null=True, default=None)   #related_name позволит получить всех связанных преподавателей для каждого кружка.
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
                
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        
        
class Awards(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='award_images/')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'
        
class Documents(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    file = models.FileField('Изображение', upload_to='documents/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        
class Licenses(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.FileField('Изображение', upload_to='licenses/')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'
        
class LeadershipContacts(models.Model):
    position = models.CharField('Должность', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    contact_info = models.CharField('Контактная информация', max_length=100)
    image = models.ImageField('Изображение', upload_to='administration_images/')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Контакт руководства'
        verbose_name_plural = 'Контакты руководства'
        
class AdmissionApplication(models.Model):
    parent_name = models.CharField('ФИО родителя', max_length=100)
    parent_contact = models.CharField('Телефон родителя', max_length=15)
    student_name = models.CharField('ФИО ученика', max_length=100)
    student_class = models.CharField('Класс', max_length=50)
    student_personal_data = models.CharField('Персональные данные ученика', max_length=150)
    parent_personal_data = models.CharField('Персональные данные родителя', max_length=150)
    attached_files = models.FileField('Прикрепленные файлы', upload_to='admission_files/')
    
    def __str__(self):
        return f'{self.student_class} {self.student_name}'
    
    class Meta:
        verbose_name = 'Заявка на поступление'
        verbose_name_plural = 'Заявки на поступление'
        
class PaidServices(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='circle_images/')
    category = models.ForeignKey('CategoriesPaidServices',  on_delete=models.SET_DEFAULT, verbose_name='Категория', null=True, default=None)  
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_width = 600
            max_height = 600

            img = Image.open(self.image.path)
            width, height = img.size

            if width > max_width or height > max_height:
                # Масштабирую изображение, если оно превышает максимальные размеры
                img.thumbnail((max_width, max_height))
                img.save(self.image.path)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'Изображение'
    
    class Meta:
        verbose_name = 'Платная услуга'
        verbose_name_plural = 'Платные услуги'   

class CategoriesPaidServices(models.Model):
    name = models.CharField('Название', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'    
        
class Questions(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField()
    message = models.TextField('Сообщение')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'    
        
        
