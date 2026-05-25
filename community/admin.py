from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'note', 'is_answered', 'created_at']
    list_filter = ['is_answered']
    search_fields = ['body']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'is_accepted', 'upvotes']
    list_filter = ['is_accepted']