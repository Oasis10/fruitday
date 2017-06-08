from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_check/$', views.login_check),
    url(r'^register_exist/$', views.register_exist),
    url(r'^info/$', views.info),
    url(r'^logout/$', views.logout),
    url(r'^add/$', views.address),

]