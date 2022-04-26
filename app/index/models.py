from django.db import models
import requests

class Task(models.Model):
    img = models.ImageField(upload_to='img', null=True, blank=True)
    title = models.CharField('Название', max_length=50)
    Description = models.TextField('Описание')


    def __str__(self):
        return self.title
        

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



class Slide(models.Model):
    img1 = models.ImageField(upload_to='img', null=True, blank=True)
    img2 = models.ImageField(upload_to='img', null=True, blank=True)
    img3 = models.ImageField(upload_to='img', null=True, blank=True)
    title = models.CharField('Название', max_length=50)
    Description = models.TextField('Описание')


    def __str__(self):
        return self.title
        

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды'


