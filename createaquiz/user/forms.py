import random

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import Profile


class UserRegisterForm(UserCreationForm):
    random_number_1 = random.randint(1, 20)
    random_number_2 = random.randint(1, 20)

    email = forms.EmailField()  # Make email a mandatory field
    captcha = forms.IntegerField(label='What is {} + {}?'.format(random_number_1, random_number_2),
                                 widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'captcha']

    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = ('activate',
                      'create',
                      'disable',
                      'login',
                      'logout',
                      'password',
                      'profile',)
        if username in disallowed:
            raise ValidationError("A user with that username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        if captcha == self.random_number_1 + self.random_number_2:
            return captcha
        else:
            raise ValidationError("That is incorrect.")

    def save(self, **kwargs):
        user = super().save(commit=False)
        user.save()
        self.save_m2m()
        Profile.objects.update_or_create(user=user, defaults={'slug': slugify(user.get_username())})
        return user
