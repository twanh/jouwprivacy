from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Index page
    url(r'^index/', views.index)

]
