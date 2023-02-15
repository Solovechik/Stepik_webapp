from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=25)
    likes = models.ManyToManyField(User)


class QuestionManager(Question):
    def new(self):
        return Question.objects.all()

    def popular(self):
        return Question.objects.all().order_by(self.rating)


class Answer(models.Model):
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
