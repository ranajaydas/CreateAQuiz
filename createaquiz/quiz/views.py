from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tag, Quiz
from .forms import TagForm, QuizForm
from .utils import PageLinksMixin


class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


class TagDetail(DetailView):
    model = Tag


class TagCreate(LoginRequiredMixin, CreateView):
    form_class = TagForm
    model = Tag


class TagUpdate(LoginRequiredMixin, UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = '_form_update'


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('quiz_tag_list')


class QuizList(PageLinksMixin, ListView):
    model = Quiz
    paginate_by = 5


class QuizDetail(DetailView):
    model = Quiz


class QuizCreate(LoginRequiredMixin, CreateView):
    form_class = QuizForm
    model = Quiz


class QuizUpdate(LoginRequiredMixin, UpdateView):
    form_class = QuizForm
    model = Quiz
    template_name_suffix = '_form_update'


class QuizDelete(LoginRequiredMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')
