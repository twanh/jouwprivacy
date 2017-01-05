from django.conf.urls import url, include
from . import views

app_name = 'info'

urlpatterns = [

    # /i/aricles/
    url(r'^articles/$', views.article_index, name='info_article_index'),

    # /i/aricles/search/
    url(r'^articles/search/$', views.article_search, name='info_article_search'),

    # /i/article/<pk>/
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='info_article_detail'),

]
