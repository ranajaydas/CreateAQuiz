import plotly.graph_objs as go
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from .models import Tag, Quiz, Question
from .forms import TagForm, QuizForm, QuestionForm
from .utils import PageLinksMixin, UserIsAuthorMixin, DeleteMixin, CreateUpdateMixin


class TagListView(ListView):
    model = Tag

    # Optimization to reduce number of database calls
    queryset = (
        Tag.objects.prefetch_related(
            'quiz_set',
        )
    )


class TagDetailView(DetailView):
    model = Tag

    # Optimization to reduce number of database calls
    queryset = (
        Tag.objects.prefetch_related(
            'quiz_set',
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
    ordering = ['-pub_date', '-id']  # Orders the posts by newest to oldest by pub-date and id

    def get_queryset(self):
        """Override of get_queryset to add search functionality."""
        query_set = super().get_queryset()

        if self.search_kwarg in self.request.GET:
            search_term = self.request.GET[self.search_kwarg]
            if search_term:
                query_set = Quiz.objects.filter(
                    Q(name__icontains=search_term)
                    | Q(description__icontains=search_term)
                    | Q(slug__icontains=search_term)
                    | Q(tags__slug__icontains=search_term)
                ).distinct()

        # search_kwarg will take precedence over user_kwarg
        elif self.user_kwarg in self.request.GET:
            user = self.request.GET[self.user_kwarg]
            if user:
                query_set = Quiz.objects.filter(author__username=user)

        # Optimization to reduce number of database calls
        return query_set.select_related('author__profile').prefetch_related('tags')


class QuizDetailView(DetailView):
    model = Quiz

    # Optimization to reduce number of database calls
    queryset = (
        Quiz.objects
            .select_related('author__profile')
            .prefetch_related('tags')
            .prefetch_related('question_set')
    )


def quiz_start_view(request, slug):
    quiz = get_object_or_404(Quiz, slug__iexact=slug)
    questions = quiz.question_set.all().order_by('?')
    form_posted = False  # Checks if the form has been posted by the user
    context = {
        'form_posted': form_posted,
        'questions': questions,
        'object': quiz,
    }

    if request.method == 'POST':
        quiz_score = 0
        quiz_total_questions = quiz.question_set.count()
        user_answer_dict = {}
        form_posted = True

        for question in questions:
            user_answer = request.POST.get(question.question_text)
            user_answer_dict[question.question_text] = user_answer
            if user_answer == question.correct_choice:
                quiz_score += 1

        quiz_score_percent = int(quiz_score / quiz_total_questions * 100)
        context.update({
            'form_posted': form_posted,
            'quiz_score': quiz_score,
            'quiz_score_percent': quiz_score_percent,
            'quiz_total_questions': quiz_total_questions,
            'user_answer_dict': user_answer_dict,
        })
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


def plotly(request):
    """Render the following pie charts and stats:
    1. Pie chart of all the quiz tags and their item count.
    2. Bar graph of questions in each quiz.
    3. Bar graph of quizzes posted per user.
    """

    # 1. Pie chart of all the quiz tags and their item count
    tags = Tag.objects.all()
    tag_names = list(tags.values_list('name', flat=True))
    quiz_count = [tag.quiz_set.count() for tag in tags]

    pie_fig = go.Figure(data=[go.Pie(
        labels=tag_names,
        values=quiz_count,
        textinfo='label+percent',
        insidetextorientation='radial'
    )])
    pie_fig_html = pie_fig.to_html(full_html=False, default_height=600, default_width=800)

    # 2. Bar graph of questions in each quiz.
    quizzes = Quiz.objects.all()
    quiz_names = [f'<a href="{quiz.get_absolute_url()}" target="_blank">{quiz.name}</a>' for quiz in quizzes]
    question_count = [quiz.question_set.count() for quiz in quizzes]
    highest_count = max(question_count)
    bar1_colors = [
        'crimson' if num_questions == highest_count else 'lightslategrey' for num_questions in question_count
    ]

    bar1_fig = go.Figure(data=[go.Bar(
        x=question_count,
        y=quiz_names,
        text=quiz_names,
        hovertemplate='<b>This quiz has %{x} questions</b><extra></extra>',
        showlegend=False,
        marker_color=bar1_colors,
        orientation='h',
    )])
    bar1_fig.update_xaxes(title_text='No. of Questions')
    bar1_fig_html = bar1_fig.to_html(full_html=False, default_height=600, default_width=800)

    # 3. Bar graph of quizzes posted per user
    users = User.objects.all()
    user_names, quiz_count, bar2_hover_text = [], [], []
    for user in users:
        user_names.append(f'<a href="{user.profile.get_absolute_url()}" target="_blank">{user.profile.name}</a>')
        count = user.quiz_set.count()
        quiz_count.append(count)
        bar2_hover_text.append(f'{count} quizzes')

    bar2_fig = go.Figure(data=[go.Bar(
        x=user_names,
        y=quiz_count,
        text=user_names,
        opacity=0.7,
        hovertemplate='<b>No. of Quizzes</b>: %{y}<extra></extra>',
        showlegend=False,
    )])
    bar2_fig.update_yaxes(title_text='No. of Quizzes')
    bar2_fig_html = bar2_fig.to_html(full_html=False, default_height=450, default_width=800)

    context = {
        'pie_fig_html': pie_fig_html,
        'bar1_fig_html': bar1_fig_html,
        'bar2_fig_html': bar2_fig_html,
    }
    return render(request, 'quiz/plotly.html', context=context)
