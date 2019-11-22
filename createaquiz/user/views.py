from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .forms import UserRegisterForm
from .utils import ProfileGetObjectMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


class ProfileUpdate(LoginRequiredMixin, ProfileGetObjectMixin, UpdateView):
    model = Profile
    fields = ('name', 'about', 'image',)


class PublicProfileDetail(DetailView):
    model = Profile
