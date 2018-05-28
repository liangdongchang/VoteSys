'''
@author ldc

'''


from django.conf.urls import url

from VoteApp import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)', views.vote),
    url(r'^share/(\d+)/$', views.share,name='shareGrade'),
    url(r'^share/grade/(\d+)/(\d+)/$', views.grade),
    url(r'^chat/', views.chat),
    url(r"^test/",views.test),
]
