from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Banner(models.Model):
    description = models.TextField()
    image1 = models.ImageField(upload_to='banner/', blank=True, null=True)
    image2 = models.ImageField(upload_to='banner/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = '7.Banner'
        ordering = ['sort']


class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = '6.Services'
        ordering = ['sort']


class Price(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = '5.Price'
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
        verbose_name = 'Blog'
        verbose_name_plural = '3.Blog'
        ordering = ['sort']


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = '8.About'
        ordering = ['sort']


class Reviews(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = '4.Reviews'
        ordering = ['sort']


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message="Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField()
    message = models.TextField()

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = '2.Contacts'
        ordering = ['-date_created']


class Session(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message="Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    email = models.EmailField()
    procedure = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        formatted_time = self.time.strftime('%H:%M')
        return f'{self.name}, {self.procedure} - {self.date} {formatted_time}'

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = '1.Sessions'
        ordering = ['-date_created']