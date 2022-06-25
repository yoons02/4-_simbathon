from asyncio.windows_events import NULL
from django.shortcuts import render, redirect, get_object_or_404
from qna.models import Professor, Department, Major, Question, Answer, Profile
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def landing(request):
    recommended_questions = Question.objects.all().order_by('-like')[:4]
    latest_questions = Question.objects.all().order_by('-pub_date')[:4]
    unsolved_questions = []
    solved_questions = []
    for q in latest_questions:
        unsolved_questions.append(q)
    for q in latest_questions:
        answers = q.answers.all()
        for a in answers:
            if a.selection == True:
                solved_questions.append(q)
                unsolved_questions.remove(q)
    return render(request, 'landing.html', {
        'recommended_questions':recommended_questions,
        'latest_questions':latest_questions,
        'unsolved_questions':unsolved_questions,
        'solved_questions':solved_questions,
    })