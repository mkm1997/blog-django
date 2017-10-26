   #it call the urls blogmkmk
from . import views

#from .models import post
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin




urlpatterns = [


   # url(r'^index/',views.index,name='index'),   #it call the function define in view

    url(r'^register/$',views.sign,name= 'register'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^blog_view/$',views.post_blog,name = 'blog_view'),
    url(r'^blog/',views.blog,name='blog'),
    url(r'^about/',views.About,name='about'),
    url(r'^user_login/$',views.user_login,name= 'user_login'),



   # url(r'^mysign/$',views.sign,name='mysign'),

  #  url(r'^logout/$',views.user_logout,name='logout'),
  #  url(r'^special/',views.special,name='special'),




    #for login and signup page

  #  url(r'^login/$', auth_views.login,name='login'),
   # url(r'^logout/$', auth_views.logout, name='logout'),


]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.MEDIA_