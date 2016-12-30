from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Admin Section/URL
    url(r'^admin/', include(admin.site.urls)),
    # Quiz section/URL
    url(r'^q/', include('quiz.urls')),
    # Info section/URL
    url(r'^i/', include('info.urls')),
    # Main section/URL !- THIS URL SHOULD BE LAST - !
    url(r'^', include('main.urls')),
]
