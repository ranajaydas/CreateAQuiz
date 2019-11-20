from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Tag, Quiz
from .forms import TagForm, QuizForm
from .utils import PageLinksMixin


class TagList(PageLinksMixin, ListView):
    model = Tag
    paginate_by = 5


class TagDetail(DetailView):
    model = Tag


class TagCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = TagForm
    model = Tag
    success_message = 'New Tag created!'


class TagUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = '_form_update'
    success_message = 'Tag updated.'


class TagDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('quiz_tag_list')
    success_message = 'Tag deleted.'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class QuizList(PageLinksMixin, ListView):
    model = Quiz
    paginate_by = 5


class QuizDetail(DetailView):
    model = Quiz


class QuizCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = QuizForm
    model = Quiz
    success_message = 'New quiz created!'


class QuizUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = QuizForm
    model = Quiz
    template_name_suffix = '_form_update'
    success_message = 'Quiz updated.'


class QuizDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')
    success_message = 'Quiz deleted.'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
