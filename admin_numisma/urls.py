from django.urls import path
from .import views 

urlpatterns = [
    path('admin_numisma/', views.admin_numisma, name='admin_numisma')
  
]
