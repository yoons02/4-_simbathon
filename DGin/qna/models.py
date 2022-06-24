from django.db import models
from django.contrib.auth.models import User

#교수
class Professor(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#학과
class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#전공(수업)
class Major(models.Model):
    name = models.CharField(max_length=20)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='majors')

    def __str__(self):
        return self.name

#질문
class Question(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to = "question/", blank=True, null=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def summary(self):
        return f"{self.body[:50]}..."

#질문에 업로드하는 이미지(미완성)
class QuestionImage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(default='media/diary/default_image.jpeg', upload_to='diary', blank=True, null=True)      

#답변
class Answer(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now=True)
    selection = models.BooleanField(default = False)

    def __str__(self):
        return self.content

#개인프로필, auth의 User를 일대일 필드로 가짐
class Profile(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department)
    introduction = models.TextField(max_length=300, blank=True, null=True)
    bookmark = models.ManyToManyField(Question)

    def __str__(self):
        return self.name
