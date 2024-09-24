from django.urls import path
from .import views 

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('home', views.home, name='home'),
    path('coins/', views.coins, name='coins'),
    path('seals/', views.seals, name='seals'),
    path('seal-issuer/', views.seal_issuer, name='seal_issuer'),
    path('sources/', views.sources, name='sources'),
    path('mints/', views.mints, name='mints'),
    path('all-datas/', views.all_datas, name='all_datas'),
]