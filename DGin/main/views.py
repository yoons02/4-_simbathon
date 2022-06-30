from asyncio.windows_events import NULL
from django.shortcuts import render, redirect, get_object_or_404
from qna.models import Professor, Department, Major, Question, Answer, Profile
from django.utils import timezone
# Create your views here.

def landing(request):
    recommended_questions = Question.objects.all()
    recommended_questions = sorted(recommended_questions, key=lambda x: -x.like_users.count())
    latest_questions = Question.objects.all().order_by('-pub_date')
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
    return render(request, 'main.html', {
        'recommended_questions1':recommended_questions[:3],
        'recommended_questions2':recommended_questions[3:6],
        'latest_questions1':latest_questions[:3],
        'latest_questions2':latest_questions[3:6],
        'unsolved_questions1':unsolved_questions[:3],
        'unsolved_questions2':unsolved_questions[3:6],
        'solved_questions1':solved_questions[:3],
        'solved_questions2':solved_questions[3:6],
    })