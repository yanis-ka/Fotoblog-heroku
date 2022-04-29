from django import forms
from . import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm      
from .models import Photo

User = get_user_model()


class PhotoForm(ModelForm):
  class Meta:
      model = Photo
      fields = ['image', 'caption']



# class BlogForm(forms.ModelForm):

#     edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

#     class Meta:
#         model = models.Blog
#         fields = ['title', 'content']



# class DeleteBlogForm(forms.Form):
#     delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)



# class FollowUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['follows']