
from django.urls import path
from .views import index , result ,prediction

urlpatterns = [
    path('', index, name='index'),
    path('prediction/result/',result,name='result'),
    path('prediction/',prediction , name='prediction')
    
]
