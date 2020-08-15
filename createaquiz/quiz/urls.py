from django.urls import path
from quiz import views

urlpatterns = [
    # Plotly charts
    path('plotly/', views.plotly_view, name='quiz_plotly'),

    # Tag URLs
    path('tag/', views.TagListView.as_view(), name='tag_list'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag/<slug>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag/<slug>/update', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag/<slug>/delete', views.TagDeleteView.as_view(), name='tag_delete'),

    # Quiz URLs
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('create/', views.QuizCreateView.as_view(), name='quiz_create'),
    path('<slug>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('<slug>/update/', views.QuizUpdateView.as_view(), name='quiz_update'),
    path('<slug>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('<slug>/begin/', views.quiz_start_view, name='quiz_start'),

    # Question URLs
    path('<quiz_slug>/question/create/', views.QuestionCreateView.as_view(), name='quiz_question_create'),
    path('<quiz_slug>/question/<int:pk>/update/', views.QuestionUpdateView.as_view(), name='quiz_question_update'),
    path('<quiz_slug>/question/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='quiz_question_delete'),
]
