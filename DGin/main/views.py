from asyncio.windows_events import NULL
from django.shortcuts import render, redirect, get_object_or_404
from qna.models import Professor, Department, Major, Question, Answer, Profile
from django.utils import timezone
# Create your views here.

def landing(request):
    recommended_questions = Question.objects.all()
    recommended_questions = sorted(recommended_questions, key=lambda x: -x.like_users.count())
    for q in recommended_questions:
        print(q.like_users.count())
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
    return render(request, 'landing.html', {
        'recommended_questions':recommended_questions[:4],
        'latest_questions':latest_questions[:4],
        'unsolved_questions':unsolved_questions[:4],
        'solved_questions':solved_questions[:4],
    })