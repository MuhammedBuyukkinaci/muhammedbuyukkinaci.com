from django.shortcuts import render

from django.views.generic import ListView 

from .models import Quiz

import json

import random

class YouKnowMeView(ListView):
    model = Quiz
    template_name = "youknowme/youknowme.html"
    context_object_name = "quizs"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['js_data'] = json.dumps(
            [
                {
                    'quiz_question': quiz.quiz_question,
                    'quiz_answer1': quiz.quiz_answer1,
                    'quiz_answer2': quiz.quiz_answer2,
                    'quiz_answer3': quiz.quiz_answer3,
                    'quiz_answer4': quiz.quiz_answer4,
                    'quiz_correct_answer': quiz.quiz_correct_answer
                }
                for quiz in sorted(Quiz.objects.all(), key=lambda x: random.random())
                
            ]
        )
        data['choices'] = range(4)
        return data