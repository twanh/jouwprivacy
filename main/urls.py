from django.conf.urls import include, url
from . import views

app_name = 'main'

urlpatterns = [
    # Index page
    url(r'^$', views.index, name='main_index')
]
