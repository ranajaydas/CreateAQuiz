from random import shuffle
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class CustomModel:
    """Common Model inherited by other models."""
    def get_model(self):
        return self.__class__.__name__


class Tag(CustomModel, models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete', kwargs={'slug': self.slug})

    def get_parent_url(self):
        return reverse('tag_list')


class Quiz(CustomModel, models.Model):
    name = models.CharField(max_length=63, db_index=True)
    slug = models.SlugField(max_length=63, unique=True, help_text='A label for URL config')
    description = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   # If user deleted, posts are not deleted

    class Meta:
        ordering = ['name']
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('quiz_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('quiz_delete', kwargs={'slug': self.slug})

    def get_start_url(self):
        return reverse('quiz_start', kwargs={'slug': self.slug})

    def create_question_url(self):
        return reverse('quiz_question_create', kwargs={'quiz_slug': self.slug})


class Question(CustomModel, models.Model):
    question_text = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=63, unique=True)
    incorrect_choice_1 = models.CharField(max_length=63, unique=True)
    incorrect_choice_2 = models.CharField(max_length=63, unique=True)
    incorrect_choice_3 = models.CharField(max_length=63, unique=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'slug': self.quiz.slug})

    def get_update_url(self):
        return reverse('quiz_question_update', kwargs={'quiz_slug': self.quiz.slug, 'pk': self.pk})

    def get_delete_url(self):
        return reverse('quiz_question_delete', kwargs={'quiz_slug': self.quiz.slug, 'pk': self.pk})

    def get_random_choices(self):
        choice_list = [self.correct_choice,
                       self.incorrect_choice_1,
                       self.incorrect_choice_2,
                       self.incorrect_choice_3]
        shuffle(choice_list)
        return choice_list
