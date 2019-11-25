from django.urls import path
from .views import (QuizListView, QuizDetailView, QuizCreateView, QuizUpdateView, QuizDeleteView, quiz_start_view,
                    QuestionCreateView, QuestionUpdateView, QuestionDeleteView,
                    TagListView, TagDetailView, TagCreateView, TagUpdateView, TagDeleteView)

urlpatterns = [
    # Tag URLs
    path('tag/', TagListView.as_view(), name='tag_list'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create'),
    path('tag/<slug>/', TagDetailView.as_view(), name='tag_detail'),
    path('tag/<slug>/update', TagUpdateView.as_view(), name='tag_update'),
    path('tag/<slug>/delete', TagDeleteView.as_view(), name='tag_delete'),

    # Quiz URLs
    path('', QuizListView.as_view(), name='quiz_list'),
    path('create/', QuizCreateView.as_view(), name='quiz_create'),
    path('<slug>/', QuizDetailView.as_view(), name='quiz_detail'),
    path('<slug>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    path('<slug>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),
    path('<slug>/begin/', quiz_start_view, name='quiz_start'),

    # Question URLs
    path('<quiz_slug>/question/create/', QuestionCreateView.as_view(), name='quiz_question_create'),
    path('<quiz_slug>/question/<int:pk>/update/', QuestionUpdateView.as_view(), name='quiz_question_update'),
    path('<quiz_slug>/question/<int:pk>/delete/', QuestionDeleteView.as_view(), name='quiz_question_delete'),
]
