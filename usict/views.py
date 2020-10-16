
from django.http import HttpResponseRedirect,HttpResponse
from  django.shortcuts import render
from usict.forms import sign_up,post,comment_blog
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'bloghtml/index1.html',{})

@login_required
def special (request):
    HttpResponse("YOU  are logged in ,have a nice day ")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog'))
def blog(request):
    return render(request,'bloghtml/blog.html',{})



# for blog post

#@login_required
def post_blog(request):

    if request.method == "POST":
        form = post(data = request.POST)
        if form.is_valid():
            pass
        form.save()
    form = post(data=request.POST)
    return render(request,'bloghtml/index1.html',{'form':form})



def comment(request):
    if request.method == "POST":
        form = comment_blog(data = request.POST)
        if form.is_valid():
            pass
        form.save()
    form = comment_blog(data=request.POST)
    return render(request,'bloghtml/index.html',{'form':form})


def About(request):
    return render(request,'bloghtml/about.html',{})







# Signup form data

def sign(request):
    registered = False

    if request.method == "POST":
        user_form= sign_up(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect(reverse('blog'))

        else:
            print(user_form.errors)
    else:
        user_form = sign_up()
    return render(request,'bloghtml/registration.html',
                                            {'user_form':user_form,
                                             'registered':registered})





# coding area for login form;

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user) #going to login
                return HttpResponseRedirect(reverse('blog'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("SUMONE TRIED TO LOGIN AND FAILD")
            print("Username:{} and paswword {}".format(username,password))

        return HttpResponse("invalid login details suppiled")

    else:
        return render(request,'bloghtml/loginmkm.html',{})





















