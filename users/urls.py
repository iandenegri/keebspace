from django.urls import path
from .views import CustomUserDetailView, CustomUserCreateView

app_name = 'users'

urlpatterns = [
    path('create', CustomUserCreateView.as_view(), name='users-create'),
    path('<int:pk>', CustomUserDetailView.as_view(), name='users-detail'),
]
