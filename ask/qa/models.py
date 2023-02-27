from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        questions = Question.questions.all().order_by('-added_at')
        return questions

    def popular(self):
        questions = Question.questions.all().order_by('-rating')
        return questions


class Question(models.Model):
    objects = models.Manager()
    questions = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def get_absolute_url(self):
        return reverse('detail_question', kwargs={'pk': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_set')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='answer_author_user')
