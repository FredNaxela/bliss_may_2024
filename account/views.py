from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from main.models import Session
from .forms import UserProfileForm


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/'


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/')


def logout_view(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile_view(request):
    user = request.user
    sessions = Session.objects.filter(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    context = {
        'user': user,
        'sessions': sessions,
        'form': form,
    }
    return render(request, 'profile.html', context)