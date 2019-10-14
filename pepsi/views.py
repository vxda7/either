from django.shortcuts import render, redirect
from .models import Question, Choice
import random
# Create your views here.


def index(request):
    numbers = Question.objects.all()
    li = []
    for i in numbers:
        li.append(i.id)

    if len(li) == 0:
        pass
    else:
        randomgame = random.choice(li)
        question = Question.objects.get(id=randomgame)
        choices = Choice.objects.filter(question=randomgame)
        context = {
            'question': question,
            'choices': choices
        }
        return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        question = Question()

        question.title = request.POST.get('title')
        question.contentA = request.POST.get('contentA')
        question.contentB = request.POST.get('contentB')
        question.urlA = request.POST.get('urlA')
        question.urlB = request.POST.get('urlB')
        question.countA = 0
        question.countB = 0
        question.save()

        return redirect('pepsi:index')
    else:
        return render(request, 'form.html')


def detail(request, id):
    question = Question.objects.get(id=id)
    choices = Choice.objects.all()
    context = {
        'question': question,
        'choices': choices
    }
    return render(request, 'detail.html', context)


def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'POST':

        question.title = request.POST.get('title')
        question.contentA = request.POST.get('contentA')
        question.contentB = request.POST.get('contentB')
        question.urlA = request.POST.get('urlA')
        question.urlB = request.POST.get('urlB')

        question.save()
        return redirect('pepsi:index')
    else:
        context = {
            'question': question
        }
        return render(request, 'form.html', context)


def delete(request, id):
    Question.objects.get(id=id).delete()

    return redirect('pepsi:index')


def new(request, id):
    tag = request.POST.get('tags')
    question = Question.objects.get(id=id)
    Choice.objects.filter(question=question)
    choice = Choice()

    choice.question = question
    choice.pick = tag
    choice.comment = request.POST.get('choice')
    if tag == 1:
        question.countA += 1
    else:
        question.countB += 1
    question.save()
    choice.save()
    return redirect("pepsi:index")


def cd(request, id):
    Choice.objects.get(id=id).delete()

    return redirect('pepsi:index')
