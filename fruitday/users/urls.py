from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^user/login/$', views.login),
    url(r'^user/register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_check/$', views.login_check),
    url(r'^register_exist/$', views.register_exist),
    url(r'^user/info/$', views.info),
    url(r'^user/logout/$', views.logout),
    url(r'^user/add/$', views.address),

]