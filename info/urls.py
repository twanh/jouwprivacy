from django.conf.urls import url, include
from . import views

app_name = 'info'

urlpatterns = [

    # /i/aricles/
    url(r'^articles/$', views.article_index, name='info_article_index'),

    # /i/article/<pk>/
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='info_article_detail'),

]
