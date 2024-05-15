from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Banner, Services, About, Price, Reviews, Blog
# from .forms import ContactForm
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        services = Services.objects.all()
        price = Price.objects.all()
        blog = Blog.objects.all()
        about = About.objects.all()
        reviews = Reviews.objects.all()

        context['banner'] = banner
        context['services'] = services
        context['price'] = price
        context['blog'] = blog
        context['about'] = about
        context['reviews'] = reviews

        return context