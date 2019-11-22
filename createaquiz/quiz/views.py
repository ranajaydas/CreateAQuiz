from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Tag, Quiz, Question
from .forms import TagForm, QuizForm, QuestionForm
from .utils import PageLinksMixin, UserIsAuthorMixin


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


def quiz_start(request, slug):
    quiz = get_object_or_404(Quiz, slug__iexact=slug)
    quiz_score = 0
    quiz_total_questions = quiz.question_set.count()
    form_posted = False

    if request.method == 'POST':
        form_posted = True
        for question in quiz.question_set.all():
            user_answer = request.POST.get(question.question_text)
            if user_answer == question.correct_choice:
                quiz_score += 1

    context = {
        'form_posted': form_posted,
        'quiz': quiz,
        'quiz_score': quiz_score,
        'quiz_total_questions': quiz_total_questions,
    }
    return render(request, 'quiz/quiz_form_start.html', context)


class QuizCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = QuizForm
    model = Quiz
    success_message = 'New quiz created!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuizUpdate(LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, UpdateView):
    form_class = QuizForm
    model = Quiz
    template_name_suffix = '_form_update'
    success_message = 'Quiz updated.'


class QuizDelete(LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')
    success_message = 'Quiz deleted.'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class QuestionCreate(LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, CreateView):
    form_class = QuestionForm
    model = Question
    success_message = 'New question created!'

    def get_initial(self):
        """Automatically associate question with correct quiz."""
        quiz_slug = self.kwargs.get('quiz_slug')
        self.quiz = get_object_or_404(Quiz, slug__iexact=quiz_slug)
        initial = {'quiz': self.quiz, }
        initial.update(self.initial)
        return initial


class QuestionUpdate(LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, UpdateView):
    form_class = QuestionForm
    model = Question
    template_name_suffix = '_form_update'
    success_message = 'Question updated.'


class QuestionDelete(LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, DeleteView):
    model = Question
    success_message = 'Question deleted.'

    def get_success_url(self):
        slug = self.kwargs.get('quiz_slug')
        return reverse_lazy('quiz_detail', kwargs={'slug': slug})

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
