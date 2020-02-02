from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('blog/<single_slug>', views.single_slug, name='single_slug'),
]
