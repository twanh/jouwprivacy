import json
import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse

from .models import Question
from .forms import QuestionForm, AddQuestion

def index(request):
    '''
    Index Page
        URL: /qa/
        :return render: index.html w/ all questions that are published
    '''

    # Gets all published questions from the database
    questions = Question.objects.filter(published=True)

    # Create the args dict for the context
    args = {}
    # Add the questions to the args dict
    args['questions'] = questions
    # Renxer the index with the published questions
    return render(request, 'qa/index.html', context=args)


def qa_list(request):
    '''
    Q&A list of all questions that are published
        URL: /qa/list/
        :return JsonResponse: json file with all published questions
    '''

    # Gets all published question form the database
    questions = Question.objects.filter(published=True)
    # Serializes the published questions to json (str)
    questions_json = serializers.serialize('json', questions)
    # Returns a JsonResponse and coverts json (str) to dict (json.loads)
    return JsonResponse(json.loads(questions_json))

# def add_question(request):
#     '''
#     Add a Q&A question
#         URL: /qa/question/add/
#         METHODS:
#             POST: Form Submitted, captcha checking and form saving
#             GET: Get the form page
#     '''

#     # Args dict for context
#     args = {}

#     # Checks if the method is POST
#     if request.method == 'POST':
#         # Fills in the form data
#         form = QuestionForm(request.POST)
#         # Checks if the form is valid
#         if form.is_valid():

#             # Verify reCAPTCHA

#             # Gets the response from the post
#             reqcaptcha_response = request.POST.get('g-recaptcha-response')
#             # Prepares the data to send to the GOOGLE reCAPTCHA API
#             data = {
#                 'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#                 'response': reqcaptcha_response
#             }
#             # POST request to the GOOGLE reCAPTCHA API
#             r = requests.post(settings.GOOGLE_RECAPTCHA_SITE_VERIFY, data=data)
#             # Json Result of the request
#             result = r.json()

#             # Checks if the reCAPTHCA is valid and saves the form
#             if result['success']:
#                 form.save()
#                 # Redirect to question page
#                 return redirect('qa_index')
#             # If not: error
#             else:
#                 args['error'] = 'reCapcha is incorrect, probeer opnieuw.'

#     else:
#         form = QuestionForm()
#         args['form'] = form
#         # args['errors'] = ''

#     args['sitekey'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
#     return render(request, 'qa/question/add.html', context=args)

def add_question(request):
    # Args dict for context
    args = {}

    # Checks if the method is post
    if request.method == 'POST':
        # Fills in the form data
        form = AddQuestion(request.POST)
        # Checks if the form is valid
        if form.is_valid():
            # Verify the reCAPTCHA

            # Gets the response from the post
            recaptcha_response = request.POST.get('g-recaptcha-response')
            # Prepare the data to be checked by google reCAPTHCA API
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
            }

            # POST request to Google reCAPTHCA API
            req = requests.post(settings.GOOGLE_RECAPTCHA_SITE_VERIFY, data=data)
            # Check if all went good
            if req.status_code == requests.codes.ok:
                # Get the result
                result = req.json()
            else:
                # If the request failed create an empty lust
                result = list()

            # Check the result of the reCAPTHCa
            if result['success']:
                # Save all the form data
                model = Question()
                model.question = form.cleaned_data['question_field']
                model.explaination = form.cleaned_data['explaination_field']
                model.catergory_field = form.cleaned_data['catergory_field']
                model.save()
                # Redirect to thank you page
                return redirect('qa_thanks')
            # If no ['success'], raise an error
            else:
                # Add a cap-error to the context args
                args['cap-error'] = 'reCapcha is ongeldig, probeer opnieuw'
                # Add the form to the context args
                args['form'] = form
    else:
        form = AddQuestion()
        args['form'] = form

    args['sitekey'] = settings.GOOGLE_RECAPTCHA_SITE_KEY
    return render(request, 'qa/question/add.html', context=args)








def question_detail(request, pk):
    '''
    Shows the details of a question
        :param pk: The primary key of the question requested
        :return render: detail page of the question
            :contect args: the question
    '''
    question = get_object_or_404(Question, pk=pk)
    args = {}
    args['question'] = question
    return render(request, 'qa/question/detail.html', context=args)


def thanks(request):
    '''
    Thanks the user for asking a question
        :return render: renders the thanks.html page
    '''
    return render(request, 'qa/thanks.html')
