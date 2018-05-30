'''
@author ldc

'''


from django.conf.urls import url

from VoteApp import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)', views.vote),
    # 显示分享主页面
    url(r'^shareNav/$', views.shareNav,name='shareNav'),
    # 显示分享者页面
    url(r'^share/(\d+)/(\d+)$', views.share,name='shareGrade'),
    # 打分
    url(r'^share/grade/', views.grade),
    # 留言
    url(r'^chat/', views.chat),
    url(r"^test/",views.test),
]
