from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpPageView(View):

    template_name = 'authentication/sign_up.html'
    form_class = forms.SignUpForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form,}
        return render(request, self.template_name, context)


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        context = {'form': form,}
        return render(request, self.template_name, context)


class UploadProfilePhotoView(LoginRequiredMixin, View):

    template_name = 'authentication/change_profile_photo.html'
    form_class = forms.UploadProfilePhotoForm

    def get(self, request):
        form = self.form_class(instance=request.user)
        context = {'form': form,}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {'form': form,}
        return render(request, self.template_name, context)
