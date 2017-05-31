from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index2),
    url(r'login', views.login)
]