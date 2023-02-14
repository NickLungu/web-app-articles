import django.forms

from .models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','announcement','anons','date_article']

        widgets = {
            'title': django.forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Article name"
            }),
            'announcement': django.forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Announcement"
            }),
            'anons': django.forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': "Article text"
            }),
            'date_article': django.forms.DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "date",
                'type':"datetime-local"
            }),
        }
