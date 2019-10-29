from django.urls import path

from .views import BuildDetailView, BuildListView

app_name = 'keebs'

urlpatterns = [
    path('', BuildListView.as_view(), name='build-list'),
    path('<int:pk>', BuildDetailView.as_view(), name='build-detail'),
]
