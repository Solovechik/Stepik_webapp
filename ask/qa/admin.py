from django.contrib import admin

from qa.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'added_at')
    ordering = ('-added_at',)
    fields = ('title', 'text', 'added_at', 'rating', 'author', 'likes')
    readonly_fields = ('added_at',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('text', 'added_at', 'question', 'author')
    readonly_fields = ('added_at',)
