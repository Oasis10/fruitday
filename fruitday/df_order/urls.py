from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.order),
    url(r'^pay/$', views.is_pay),
]