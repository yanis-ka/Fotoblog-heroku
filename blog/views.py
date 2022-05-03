from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import forms, models
from django.forms import formset_factory
from django.db.models import Q 
from cloudinary.forms import cl_init_js_callbacks 

@login_required
def home(request):
    photos = models.Photo.objects.all()
    context={'photos': photos}
    return render(request, 'blog/home.html', context)


class PhotoUploadView(LoginRequiredMixin, View):
    # permission_required = 'blog.add_photo'
    template_name = 'blog/photo_upload.html'
    form_class = forms.PhotoForm
    
    def get(self, request):
        form = self.form_class()
        context = {'form': form,}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
        context = {'form': form,}
        return render(request, self.template_name, context)


class BlogAndPhotoUploadView(LoginRequiredMixin, View):
    # permission_required = ('blog.add_blog', 'blog.add_photo')
    template_name = 'blog/create_post_blog.html'
    blog_form_class = forms.BlogForm
    photo_form_class = forms.PhotoForm

    def get(self, request):
        blog_form = self.blog_form_class()
        photo_form = self.photo_form_class()
        context = {
            'blog_form': blog_form,
            'photo_form': photo_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        blog_form = self.blog_form_class(request.POST)
        photo_form = self.photo_form_class(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.photo = photo
            blog.author = request.user
            blog.save()
            # blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur principal'})
            return redirect('home')
        context = {
            'blog_form': blog_form,
            'photo_form': photo_form,
        }
        return render(request, self.template_name, context)