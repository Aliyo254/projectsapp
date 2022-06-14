from . import views
from django.conf.urls import url


urlpatterns=[
       url(r'^$',views.home,name='Home'),
       url(r'^new_project',views.new_project,name='new_project'),
]