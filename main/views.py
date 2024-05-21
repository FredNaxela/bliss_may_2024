from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Banner, Services, About, Price, Reviews, Blog
from .forms import ContactForm
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

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('main:index')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)