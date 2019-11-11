from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm

# Create your views here.

class CustomUserDetailView(DetailView):

    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(CustomUserDetailView, self).get_context_data(**kwargs)
        return context

class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'users/create.html'
