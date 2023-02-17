from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')


class QuestionManager(Question):
    def new(self):
        return Question.objects.all()

    def popular(self):
        return Question.objects.all().order_by(self.rating)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
