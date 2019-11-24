from django import forms
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError
from .models import Tag, Quiz, Question

slugs_not_allowed = ['create', 'tag', ]


class SlugCleanMixin:
    """Mixin class for slug cleaning methods."""

    def clean_slug(self):
        """Ensure all slugs are lowercase and not in 'slugs_not_allowed'."""
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug in slugs_not_allowed:
            raise ValidationError("Slug may not be {}.".format(new_slug))
        return new_slug


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        """Ensure all tag 'names' are lowercase."""
        return self.cleaned_data['name'].lower()


class QuizForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ('author',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {'quiz': HiddenInput()}
