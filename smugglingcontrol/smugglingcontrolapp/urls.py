from django.conf.urls import url
from django.urls import path
from smugglingcontrolapp import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('about/', views.about_view),
    
   
]