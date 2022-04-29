from itertools import chain
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from . import forms, models
from django.forms import formset_factory
from django.db.models import Q 

@login_required
def home(request):
    return render(request, 'blog/home.html')