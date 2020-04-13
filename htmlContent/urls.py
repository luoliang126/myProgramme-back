from django.urls import path
from htmlContent.views import index

urlpatterns = [
    path('index/', index),
]