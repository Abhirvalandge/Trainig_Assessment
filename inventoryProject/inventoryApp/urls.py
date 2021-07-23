from django.urls import path
from .views import *

urlpatterns = [
        path('category-view/', CategoryView.as_view()),    
        path('product-view/', ProductView.as_view()),    
    
]
