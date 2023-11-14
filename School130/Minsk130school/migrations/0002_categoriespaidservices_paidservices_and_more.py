# Generated by Django 4.2.4 on 2023-11-13 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Minsk130school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesPaidServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PaidServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='circle_images/', verbose_name='Изображение')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Minsk130school.categoriespaidservices', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Платная услуга',
                'verbose_name_plural': 'Платные услуги',
            },
        ),
        migrations.AddField(
            model_name='teachers',
            name='paid_service',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Minsk130school.paidservices', verbose_name='Платные услуги'),
        ),
    ]
