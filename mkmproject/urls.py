"""mkmproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from usict import views

#from django.contrib.auth import views as auth_views


urlpatterns = [
   # url(r'^$',views.index,name='index'),
    #url(r'$',views.PostListView.as_view(),name='post_list'),
    #url(r'^about/$',views.AboutView.as_view(),name='about'),
    #url(r'^post/(?P<pk>\d+)$',views.PostDeatilView.as_view(),name='post_detail'),
    #url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$',views.CreatePostView.as_view(),name='post_edit'),
    #url(r'^post/(?P<pk>\d+)/remove/$',views.CreatePostView.as_view(),name='post_remove'),

    url(r'^admin/', admin.site.urls),
    url(r'^usict/', include('usict.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/',views.special,name ='special'),
]
