
from django.contrib import admin

# Register your models here.
from .models import usersignup,blog_post,blog_comment

#admin.site.register(post)
admin.site.register(blog_post)
admin.site.register(usersignup)
admin.site.register(blog_comment)