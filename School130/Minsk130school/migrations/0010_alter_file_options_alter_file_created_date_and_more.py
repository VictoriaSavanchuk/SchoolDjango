# Generated by Django 4.2.4 on 2023-11-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minsk130school', '0009_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterField(
            model_name='file',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.FileField(upload_to='uploads/files', verbose_name='Путь'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
