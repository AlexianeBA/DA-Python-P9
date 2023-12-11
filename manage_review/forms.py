from django import forms
from .models import Article, ArticleImage
from multiupload.fields import MultiFileField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)