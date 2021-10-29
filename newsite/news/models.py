from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=64)
    anons = models.CharField('Анонс', max_length=192)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'