from django.urls import path
from .import views 
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    path('', views.Index, name='index'),
    path('adopt/', Adopt, name='adopt'),
    path('service/', views.Service, name='service'),
    path('service/index.html', views.Index, name='index'),
    path('service/services/', views.Services, name='services'),
    path('services/', views.Services, name='services'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('gallary/', views.Gallary, name='gallary'),
    path('save-enquiry', views.saveEnquiry, name='save-enquiry'),
    path('news-letter', views.newsLetter, name='news-letter'),
    path('conta-ct', views.contacts, name='conta-ct'),
    path('about/contact.html/', views.contacts, name='contact'),
    path('about/service.html', views.Service, name='service'),
    path('about/gallary.html/', views.Gallary, name='gallary'),

    path('about/Adopt.html/', views.Adopt, name='adopt'),
    path('about/index.html/', views.Index, name='index'),
    path('about/index.html/', views.Index, name='index'),

    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
   
   

    path('adoptform/',views.adoptform, name='adoptform'),
    path('donate/', views.donate, name='donate'),

   

    path('about/donate/', views.donate, name='donate'),
    
]
