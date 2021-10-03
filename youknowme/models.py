from django.db import models

# Create your models here.
# Welcome Page Text
class Quiz(models.Model):

    quiz_question = models.CharField(max_length=200)
    quiz_answer1 = models.CharField(max_length=50)
    quiz_answer2 = models.CharField(max_length=50)
    quiz_answer3 = models.CharField(max_length=50)
    quiz_answer4 = models.CharField(max_length=50)
    quiz_correct_answer = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz_question