from django import forms
from .models import Note, Category


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'text']

        #  настройка HTML ('rows': 10 сделать поле текста в 10 строк, 'placeholder' подсказка в поле ввода)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Пиши свои мысли здесь...'}),
            'title': forms.TextInput(attrs={'placeholder': 'Тема заметки'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']