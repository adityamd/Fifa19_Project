from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    url(r'^$',views.home),
    url(r'getBid/$',views.getBidding)
]
urlpatterns += staticfiles_urlpatterns()