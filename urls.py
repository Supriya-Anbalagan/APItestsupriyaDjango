"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register/',views.registerviewset.as_view({'get':'list','post':'create'})),
    path('Register/',<int:pk>/'views.registerviewset.as_view({'delete':'destroy'})),
 
    path('Password/',views.Passwordviewset.as_view({'get':'list','post':'create'})),
    path('Password/',<int:pk>/'views.Passwordviewset.as_view({'delete':'destroy'})),
 
    path('Deposit/',views.Depositviewset.as_view({'get':'list','post':'create'})),
    path('Deposit/',<int:pk>/'views.Depositviewset.as_view({'delete':'destroy'})),
   
    path('Withdraw/',views.Withdrawviewset.as_view({'get':'list','post':'create'})),
    path('Withdraw/',<int:pk>/'views.Withdrawviewset.as_view({'delete':'destroy'})),

    path('Register/',views.registerviewset.as_view({'get':'list','post':'create'})),
    path('Register/',<int:pk>/'views.registerviewset.as_view({'delete':'destroy'})),
   
   path('api-auth/', include('rest-framework.urls', names-space='rest_framework'))

]
