# Generated by Django 4.2.4 on 2023-11-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minsk130school', '0008_rename_file_licenses_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file_path', models.FileField(upload_to='uploads/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]