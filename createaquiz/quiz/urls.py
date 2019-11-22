from django.urls import path
from .views import (QuizList, QuizDetail, QuizCreate, QuizUpdate, QuizDelete, quiz_start,
                    QuestionCreate, QuestionUpdate, QuestionDelete,
                    TagList, TagDetail, TagCreate, TagUpdate, TagDelete)

urlpatterns = [
    # Quiz URLs
    path('', QuizList.as_view(), name='quiz_list'),
    path('create/', QuizCreate.as_view(), name='quiz_create'),
    path('<slug>/', QuizDetail.as_view(), name='quiz_detail'),
    path('<slug>/update', QuizUpdate.as_view(), name='quiz_update'),
    path('<slug>/delete', QuizDelete.as_view(), name='quiz_delete'),
    path('<slug>/begin', quiz_start, name='quiz_start'),

    # Question URLs
    path('<quiz_slug>/question/create/', QuestionCreate.as_view(), name='quiz_question_create'),
    path('<quiz_slug>/question/<int:pk>/update', QuestionUpdate.as_view(), name='quiz_question_update'),
    path('<quiz_slug>/question/<int:pk>/delete', QuestionDelete.as_view(), name='quiz_question_delete'),

    # Tag URLs
    path('tag', TagList.as_view(), name='quiz_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='quiz_tag_create'),
    path('tag/<slug>/', TagDetail.as_view(), name='quiz_tag_detail'),
    path('tag/<slug>/update', TagUpdate.as_view(), name='quiz_tag_update'),
    path('tag/<slug>/delete', TagDelete.as_view(), name='quiz_tag_delete'),
]
