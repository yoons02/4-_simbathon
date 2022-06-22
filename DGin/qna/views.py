from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.utils import timezone
# Create your views here.

def majorList(request):
    return render(request, 'qna/majorList.html')

def nonmajorList(request):
    return render(request, 'qna/nonmajorList.html')

def detail(request, id):
    question = get_object_or_404(Question, pk = id)
    all_answers = question.answers.all().order_by('-created_at')
    return render(request, 'qna/detail.html', {'question':question, 'answers':all_answers})

def new(request):
    return render(request, 'qna/new.html')

def create(request):
    new_question = Question()
    new_question.title = request.Question['title']
    new_question.writer = request.user
    new_question.pub_date = timezone.now()
    new_question.body = request.Question['body']
    new_question.image = request.FILES.get('image')
    new_question.save()
    return redirect('qna:detail', new_question.id)

def edit(request, id):
    edit_question = Question.objects.get(id = id)
    return render(request, 'qna/edit.html', {'question' : edit_question})

def update(request, id):
    update_question = Question.objects.get(id=id)
    update_question.title = request.POST['title']
    update_question.writer =  request.user
    update_question.pub_date = timezone.now()
    update_question.body = request.POST['body']
    update_question.image = request.FILES.get('image')
    update_question.save()
    return redirect('qna:detail', update_question.id)

def delete(request , id):
    delete_question = Question.objects.get(id = id)
    delete_question.delete()
    return redirect('qna:index')

def create_answer(request, question_id):
    new_answer = Answer()
    new_answer.writer = request.user
    new_answer.content = request.POST['content']
    new_answer.question = get_object_or_404(Question, pk=question_id)
    new_answer.save()
    return redirect('qna:detail', question_id)

def edit_answer(request, question_id, answer_id):
    target_question = Question.objects.get(id = question_id)
    edit_answer = Answer.objects.get(id = answer_id)
    return render(request, 'qna/edit_answer.html', {'question':target_question, 'answer' : edit_answer})

def update_answer(request, question_id, answer_id):
    target_question = Question.objects.get(id = question_id)
    update_answer = Answer.objects.get(id = answer_id)
    update_answer.content = request.POST['content']
    update_answer.writer =  request.user
    update_answer.save()
    return redirect('qna:detail', target_question.id)
  
def delete_answer(request , question_id, answer_id):
    target_question = Question.objects.get(id = question_id)
    delete_answer = Answer.objects.get(id = answer_id)
    delete_answer.delete()
    return redirect('qna:detail', target_question.id)