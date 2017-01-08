from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.log_in, name='log_in'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^save_score/$', views.save_score, name ='save_score'),
    url(r'^log_out/$', views.log_out, name='log_out'),

]
