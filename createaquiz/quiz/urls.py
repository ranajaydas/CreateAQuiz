from django.urls import path
from .views import (QuizList, QuizDetail, QuizCreate, QuizUpdate, QuizDelete,
                    TagList, TagDetail, TagCreate, TagUpdate, TagDelete)

urlpatterns = [
    path('', QuizList.as_view(), name='quiz_list'),
    path('create/', QuizCreate.as_view(), name='quiz_create'),
    path('<slug>/', QuizDetail.as_view(), name='quiz_detail'),
    path('<slug>/update', QuizUpdate.as_view(), name='quiz_update'),
    path('<slug>/delete', QuizDelete.as_view(), name='quiz_delete'),
    path('tag', TagList.as_view(), name='quiz_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='quiz_tag_create'),
    path('tag/<slug>/', TagDetail.as_view(), name='quiz_tag_detail'),
    path('tag/<slug>/update', TagUpdate.as_view(), name='quiz_tag_update'),
    path('tag/<slug>/delete', TagDelete.as_view(), name='quiz_tag_delete'),
]
