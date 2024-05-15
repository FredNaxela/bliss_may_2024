from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Banner(models.Model):
    description = models.TextField()
    image1 = models.ImageField(upload_to='banner/', blank=True, null=True)
    image2 = models.ImageField(upload_to='banner/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннери'
        ordering = ['sort']


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'
        ordering = ['sort']


class Price(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ціна'
        verbose_name_plural = 'Ціни'
        ordering = ['sort']


class Blog(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['sort']


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'
        ordering = ['sort']


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'
        ordering = ['sort']