from django import forms
from .models import blog_post,blog_comment
from django.contrib.auth.models import User




class sign_up(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class post(forms.ModelForm):


    class Meta():
        model = blog_post
        fields = ('name','title','text')
        widget = {
            'text':forms.Textarea(attrs={'class':'blog_body'})
        }


class comment_blog(forms.ModelForm):
    class Meta():
        model = blog_comment
        fields = ('name','email','message')



''' class PostForm(forms.ModelForm):

    class Meta():
        model = post
        fields = ('author','title','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'body': forms.Textarea(attrs={'class': 'editable medium-editer-textarea postcontent'})
        }


class commentform(forms.ModelForm):


    class Meta():
        model = comment
        fields = ('author','message')
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'message':forms.Textarea(attrs= {'class' :'editable medium-editer-textarea'})
        }

'''





''' class mysign(forms.ModelForm):
    class Meta():
        model = signup
        fields = "__all__" '''

