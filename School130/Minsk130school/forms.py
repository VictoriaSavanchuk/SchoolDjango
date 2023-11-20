from django import forms
from .models import Questions, AdmissionApplication

class QuestionsForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Ваш email'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}))

    class Meta:
        model = Questions
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class AdmissionApplicationForm(forms.ModelForm):
    parent_name = forms.CharField(label=' ', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ФИО родителя', 'class': 'form-control'}))
    parent_contact = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Телефон родителя: +375 ХХ ХХХ ХХ ХХ', 'class': 'form-control'}))
    student_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ФИО ученика', 'class': 'form-control'}))
    student_class = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Класс', 'class': 'form-control'}))
    student_personal_data = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Персональные данные ученика', 'class': 'form-control'}))
    parent_personal_data = forms.CharField(label='', max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Персональные данные родителя', 'class': 'form-control'}))
    attached_files = forms.FileField(label='', widget=forms.ClearableFileInput(attrs={'placeholder': 'Добавить файл', 'class': 'form-control'}))
   
    class Meta:
        model = AdmissionApplication
        fields = ['parent_name', 'parent_contact', 'student_name', 'student_class', 
                  'student_personal_data', 'parent_personal_data', 'attached_files']
        
class DisplayForm(forms.Form):
    DISPLAY_CHOICES = [
        ('awards', 'Награды'),
        ('licenses', 'Лицензии')
    ]

    display_option = forms.ChoiceField(label='', choices=DISPLAY_CHOICES) 