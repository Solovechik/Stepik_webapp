from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

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


@require_GET
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question
    }
    return render(request, 'qa/question_detail.html', context=context)
