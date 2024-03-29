# Generated by Django 4.2.4 on 2023-11-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=100, verbose_name='Имя родителя')),
                ('parent_contact', models.CharField(max_length=100, verbose_name='Контактный телефон родителя')),
                ('student_name', models.CharField(max_length=100, verbose_name='Имя ученика')),
                ('student_class', models.CharField(max_length=50, verbose_name='Класс')),
                ('student_personal_data', models.TextField(verbose_name='Персональные данные ученика')),
                ('parent_personal_data', models.TextField(verbose_name='Персональные данные родителя')),
                ('attached_files', models.FileField(upload_to='admission_files/', verbose_name='Прикрепленные файлы')),
            ],
            options={
                'verbose_name': 'Заявки на поступление',
                'verbose_name_plural': 'Заявки на поступление',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='award_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Награда',
                'verbose_name_plural': 'Награды',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('publicationDate', models.DateField(blank=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(upload_to='blog_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('file', models.FileField(upload_to='documents/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='LeadershipContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('contact_info', models.CharField(max_length=100, verbose_name='Контактная информация')),
            ],
            options={
                'verbose_name': 'Контакты руководства',
                'verbose_name_plural': 'Контакты руководства',
            },
        ),
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('file', models.FileField(upload_to='licenses/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Лицензия',
                'verbose_name_plural': 'Лицензии',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='teacher_images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
    ]
