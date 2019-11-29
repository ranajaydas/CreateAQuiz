from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from .models import Tag, Quiz, Question
from .forms import TagForm, QuizForm, QuestionForm
from .utils import PageLinksMixin, UserIsAuthorMixin, DeleteMixin, CreateUpdateMixin


class TagListView(ListView):
    model = Tag
    queryset = (
        Tag.objects
        .prefetch_related('quiz_set',
                          )
    )


class TagDetailView(DetailView):
    model = Tag

    # Optimization to reduce number of database calls
    queryset = (
        Tag.objects
        .prefetch_related('quiz_set',
                          'quiz_set__author',
                          )
    )


class TagCreateView(CreateUpdateMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TagForm
    model = Tag
    success_message = 'New Tag created!'
    permission_required = '.add_tag'
    page_title = 'Create Tag'


class TagUpdateView(CreateUpdateMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = TagForm
    model = Tag
    success_message = 'Tag updated.'
    permission_required = '.change_tag'
    page_title = 'Update Tag'


class TagDeleteView(DeleteMixin, LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag_list')
    success_message = 'Tag deleted.'
    permission_required = '.delete_tag'


class QuizListView(PageLinksMixin, ListView):
    model = Quiz
    paginate_by = 6
    ordering = ['-pub_date', '-id']             # Orders the posts by newest to oldest by pub-date and id
    search_kwarg = 'q'

    def get_queryset(self):
        """Override of get_queryset to add search functionality."""
        query_set = super().get_queryset()
        if self.search_kwarg in self.request.GET:
            search_term = self.request.GET[self.search_kwarg]
            if search_term:
                query_set = Quiz.objects.filter(
                    Q(name__contains=search_term)
                    | Q(description__icontains=search_term)
                    | Q(slug__icontains=search_term)
                )
        # Optimization to reduce number of database calls
        return query_set.select_related('author').prefetch_related('tags')


class QuizDetailView(DetailView):
    model = Quiz

    # Optimization to reduce number of database calls
    queryset = (
        Quiz.objects
        .select_related('author')
        .prefetch_related('tags')
    )


def quiz_start_view(request, slug):
    quiz = get_object_or_404(Quiz, slug__iexact=slug)
    quiz_score = 0
    quiz_total_questions = quiz.question_set.count()
    form_posted = False     # Checks if the form has been posted by the user

    if request.method == 'POST':
        form_posted = True
        for question in quiz.question_set.all():
            user_answer = request.POST.get(question.question_text)
            if user_answer == question.correct_choice:
                quiz_score += 1

    context = {
        'form_posted': form_posted,
        'object': quiz,
        'quiz_score': quiz_score,
        'quiz_total_questions': quiz_total_questions,
    }
    return render(request, 'quiz/quiz_start_form.html', context)


class QuizCreateView(CreateUpdateMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = QuizForm
    model = Quiz
    success_message = 'New quiz created!'
    page_title = 'Create Quiz'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuizUpdateView(CreateUpdateMixin, LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, UpdateView):
    form_class = QuizForm
    model = Quiz
    success_message = 'Quiz updated.'
    page_title = 'Update Quiz'


class QuizDeleteView(DeleteMixin, LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz_list')
    success_message = 'Quiz deleted.'


class QuestionCreateView(CreateUpdateMixin, LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, CreateView):
    form_class = QuestionForm
    model = Question
    success_message = 'New question created!'
    page_title = 'Create Question'

    def get_initial(self):
        """Automatically associate question with correct quiz."""
        quiz_slug = self.kwargs.get('quiz_slug')
        self.quiz = get_object_or_404(Quiz, slug__iexact=quiz_slug)
        initial = {'quiz': self.quiz, }
        initial.update(self.initial)
        return initial


class QuestionUpdateView(CreateUpdateMixin, LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, UpdateView):
    form_class = QuestionForm
    model = Question
    success_message = 'Question updated.'
    page_title = 'Update Question'


class QuestionDeleteView(DeleteMixin, LoginRequiredMixin, UserIsAuthorMixin, SuccessMessageMixin, DeleteView):
    model = Question
    success_message = 'Question deleted.'

    def get_success_url(self):
        slug = self.kwargs.get('quiz_slug')
        return reverse_lazy('quiz_detail', kwargs={'slug': slug})
