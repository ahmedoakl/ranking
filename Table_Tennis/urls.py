from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/?$', views.login_view, name="login_view"),
    url(r'^register/?$', views.register_view, name="register_view"),
]