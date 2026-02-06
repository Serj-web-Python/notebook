from django import forms
from .models import Note, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'text']  # Поля, которые заполняет юзер
        # Обрати внимание: поля 'user' здесь НЕТ. Мы не даем юзеру выбрать владельца.

        #  настройка HTML ('rows': 10 сделать поле текста в 10 строк, 'placeholder' подсказка в поле ввода)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Пиши свои мысли здесь...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Тема заметки'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


#  Создаем улучшенную форму регистрации
class CustomUserCreationForm(UserCreationForm):
    # Добавляем поле Email и делаем его обязательным (required=True)
    email = forms.EmailField(required=True, label="Email адрес")

    class Meta:
        model = User
        # Перечисляем поля, которые хотим видеть (пароли Django добавит сам)
        fields = ('username', 'email')
