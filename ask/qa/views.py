from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET

from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
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
        'user': request.user,
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
            form.cleaned_data['author'] = request.user
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
            form.cleaned_data['author'] = request.user
            new_question = form.save()
            return redirect(reverse('detail_question', kwargs={'pk': new_question.pk}))
    else:
        form = AskForm()

    context = {
        'form': form
    }

    return render(request, 'qa/ask_question.html', context)


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.clean()
            username = request.POST['username']
            password = request.POST['password']
            User.objects.create_user(**form.cleaned_data)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('new_questions')
    else:
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'qa/signup.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.clean()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('new_questions')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'qa/login.html', context=context)
