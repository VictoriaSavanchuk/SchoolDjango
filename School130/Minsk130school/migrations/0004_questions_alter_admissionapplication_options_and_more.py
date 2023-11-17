# Generated by Django 4.2.4 on 2023-11-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minsk130school', '0003_teachers_brief_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AlterModelOptions(
            name='admissionapplication',
            options={'verbose_name': 'Заявка на поступление', 'verbose_name_plural': 'Заявки на поступление'},
        ),
        migrations.AlterModelOptions(
            name='leadershipcontacts',
            options={'verbose_name': 'Контакт руководства', 'verbose_name_plural': 'Контакты руководства'},
        ),
    ]
