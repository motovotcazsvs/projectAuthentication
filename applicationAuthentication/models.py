from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title_book = models.CharField('Название книги', max_length = 100, blank=True, null=True)
    author_book = models.CharField('Автор книги',  max_length = 100, blank=True, null=True)
    date_book = models.IntegerField(verbose_name = 'Год книги', blank=True, null=True)
    description_book = models.TextField('Описание книги', max_length = 2000, blank = True,)
    image_book = models.ImageField(blank = True, upload_to = 'image/', verbose_name = 'Изображение книги')
    pdf_book = models.FileField(blank = True, upload_to = 'pdf/', verbose_name = 'Ссылка pdf')
    date_publication = models.DateTimeField('Дата публикации', auto_now_add = True, db_index = True, blank=True, null=True)
    author_publication = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор книги', 
    blank = True, null = True) 
    like_publication = models.BigIntegerField('Себе', default = False) 
    like_author = models.BooleanField(default = False)

    def __str__(self):
        return self.title_book

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'