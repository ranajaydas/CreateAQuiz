from django.contrib import admin
from .models import Tag, Quiz, Question, Choice

admin.site.register(Tag)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
