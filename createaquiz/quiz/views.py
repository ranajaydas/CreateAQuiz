from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class TagCreate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TagForm
    model = Tag
    success_message = 'New Tag created!'
    permission_required = 'quiz.add_tag'


class TagUpdate(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = '_form_update'
    success_message = 'Tag updated.'
    permission_required = 'quiz.change_tag'


class TagDelete(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('quiz_tag_list')
    success_message = 'Tag deleted.'
    permission_required = 'quiz.delete_tag'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class QuizList(PageLinksMixin, ListView):
    model = Quiz
    paginate_by = 5


class QuizDetail(DetailView):
    model = Quiz


class QuizCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = QuizForm
    model = Quiz
    success_message = 'New quiz created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuizUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = QuizForm
    model = Quiz
    template_name_suffix = '_form_update'
    success_message = 'Quiz updated.'


class QuizDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')
    success_message = 'Quiz deleted.'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
