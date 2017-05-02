from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from django.core import serializers
from django.http import JsonResponse
import json
from .modles import Question


def index(request):
    questions = Question.objects.all()
    args = {}
    args['questions'] = questions
    return render(request, 'qa/index.html', context=args)


def qa_list(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return JsonResponse(json.loads(questions_json))

def add_question(request):
    if request.method == 'POST':
        # Verify reCAPTCHA
        # Save form
    else:
        # render form
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'qa/question/detail.html')
