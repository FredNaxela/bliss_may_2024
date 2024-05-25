from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Banner, Services, About, Price, Reviews, Blog
from .forms import ContactForm, SessionForm
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
        contact_form = ContactForm()
        session_form = SessionForm()

        context['banner'] = banner
        context['services'] = services
        context['price'] = price
        context['blog'] = blog
        context['about'] = about
        context['reviews'] = reviews
        context['contact_form'] = contact_form
        context['session_form'] = session_form

        return context

    def post(self, request, *args, **kwargs):
        if 'submit_contact_form' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Your message was sent successfully!', extra_tags='contact')
                return redirect('main:index')
            else:
                context = self.get_context_data()
                context['contact_form'] = contact_form
                messages.error(request, 'Please correct the errors.')
                return self.render_to_response(context)

        elif 'submit_session_form' in request.POST:
            session_form = SessionForm(request.POST)
            if session_form.is_valid():
                session_form.save()
                messages.success(request, 'You have signed up for a session!', extra_tags='session')
                return redirect('main:index')
            else:
                context = self.get_context_data()
                context['session_form'] = session_form
                return self.render_to_response(context)

        else:
            context = self.get_context_data()
            return self.render_to_response(context)