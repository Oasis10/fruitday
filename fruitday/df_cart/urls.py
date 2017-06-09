# from django.conf.urls import url
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^add/$', views.add),
    url(r'^$', views.list),
    url(r'count_change/$', views.count_change),
    url(r'delete/$', views.delete),
    url(r'order/$', views.order)
]