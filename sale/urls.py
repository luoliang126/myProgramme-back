from django.urls import path
from sale.views import index,index1,index2

urlpatterns = [
    path('index/', index),
    path('index1/', index1),
    path('index2/', index2),
]