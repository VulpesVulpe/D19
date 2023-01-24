from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'category',
           'name'
       ]
       labels = {'title': 'Заголовок публикации',
                 'text': 'Текст публикации',
                 'category': 'Категория публикации',
                 'name': 'Автор публикации'
        }
       widgets = {
           'text': SummernoteWidget(),
       }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'user')

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}