from django.urls import path
from loginContent.views import login

urlpatterns = [
    path('login/', login),
]