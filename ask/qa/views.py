from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET

from qa.forms import AskForm, AnswerForm
from qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def get_new_questions(request):
    questions = Question.questions.new()
    paginator = Paginator(questions, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'qa/index.html', context)


@require_GET
def get_popular_questions(request):
    questions = Question.questions.popular()
    paginator = Paginator(questions, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'qa/index.html', context)


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.clean()
            new_answer = form.save()
            return redirect(reverse('detail_question', kwargs={'pk': new_answer.question.pk}))
    else:
        form = AnswerForm()

    context = {
        'question': question,
        'form': form
    }
    return render(request, 'qa/question_detail.html', context=context)


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form.clean()
            new_question = form.save()
            return redirect(reverse('detail_question', kwargs={'pk': new_question.pk}))
    else:
        form = AskForm()

    context = {
        'form': form
    }

    return render(request, 'qa/ask_question.html', context)
