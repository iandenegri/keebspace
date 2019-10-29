from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import CustomUser

# Create your views here.

class CustomUserDetailView(DetailView):

    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(CustomUserDetailView, self).get_context_data(**kwargs)
        return context
