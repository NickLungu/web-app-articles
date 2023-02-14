from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    announcement = models.CharField('Announcement', max_length=256)
    anons = models.TextField('Article')
    date_article = models.DateTimeField('Publication date')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title