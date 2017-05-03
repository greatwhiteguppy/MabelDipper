from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^appointments$', views.appointments, name = "appointments"),
        url(r'^addtask$', views.addtask),
        url(r'^remove/(?P<id>\d+)$', views.remove),
        url(r'^appointments/(?P<id>\d+)$', views.edit),
        url(r'^logout$', views.logout_view, name ="logout"),
]
