from django.db import models
from django.shortcuts import reverse


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('quiz_tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('quiz_tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('quiz_tag_delete', kwargs={'slug': self.slug})


class Quiz(models.Model):
    name = models.CharField(max_length=63, db_index=True)
    slug = models.SlugField(max_length=63, unique=True, help_text='A label for URL config')
    description = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

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


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)
    incorrect_answer1 = models.CharField(max_length=100)
    incorrect_answer2 = models.CharField(max_length=100)
    incorrect_answer3 = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text
