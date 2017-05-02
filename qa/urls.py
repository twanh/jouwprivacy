from django.conf.urls import url, include
from . import views

app_name = 'qa'

urlpatterns = [

    # Q&A Index page, shows a list of all published questions
    # URL: /qa/
    url(r'^$', views.index, name='qa_index'),
    # Q&A Json list page, for possible references on other pages
    # URL: /qa/list/
    url(r'^list/$', views.qa_list, name='qa_list'),
    # Q&A add question page
    # URL: /qa/question/add/#
    url(r'^question/add/', views.add_question, name='qa_add_question'),
    # Q&A Full question details, shows the full question + the awnser
    # URL: /qa/question/<pk>/
    url(r'^question/(?P<pk>[0-9]+)/$', views.question_detail, name='qa_question_detail'),
    # Q&A Thanx for the question
    # URL: /qa/thanks/
    url(r'^/thanks/', views.thanks, name='qa_thanks'),
 ]
