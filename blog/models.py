from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category', max_length=255)
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text')
    created_at = models.DateTimeField('Date', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField('Name', max_length=30, default='Unknown')
    text = models.TextField('Comment')
    post = models.ForeignKey(Post, verbose_name='Tagged Post', on_delete=models.PROTECT)
    created_at = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return self.text[:10]

