from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('questions/', views.question_board, name='question_board'),
    path('question/<int:pk>/answer/', views.add_answer, name='add_answer'),
    path('answer/<int:pk>/upvote/', views.upvote_answer, name='upvote_answer'),
    path('answer/<int:pk>/accept/', views.accept_answer, name='accept_answer'),
]