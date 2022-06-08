from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='home'),
    # path('about/', views.about, name='about'),  
    # path('contact/', views.contact, name='contact'),
    # path('blog/', views.blog, name='blog'),
]