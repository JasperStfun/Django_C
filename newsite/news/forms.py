from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'text', 'pub_date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            'pub_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
        }