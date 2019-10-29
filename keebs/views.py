from django.shortcuts import render, HttpResponse
from django.views.generic import DetailView, TemplateView, ListView

from .models import Build

# Create your views here.


class HomeTemplateView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_builds'] = Build.objects.all()[:5]
        return context

class BuildListView(ListView):
    model = Build
    context_object_name = 'builds'
    template_name='keebs.build_list.html'

class BuildDetailView(DetailView):

    model = Build

    def get_context_data(self, **kwargs):
        context = super(BuildDetailView, self).get_context_data(**kwargs)
        return context