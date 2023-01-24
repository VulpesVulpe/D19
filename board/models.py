from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.urls import reverse




class Users(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name.username


class Post(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField("Category", through='PostCategory', verbose_name='Категория')
    title = models.CharField(max_length=90, verbose_name='Заголовок')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.title.title()}: {self.text[:100]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, through='CategoryUser')

    def __str__(self):
        return self.name.title()


class CategoryUser(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)