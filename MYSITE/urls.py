"""MYSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='Index'),
    path('about', views.about, name='About'),

    #Extra-tool
    path('calculator',views.calculator,name = 'Calculator'),

    # Mathematics
    path('algebra', views.algebra, name='Algebra'),
    path('pre-algebra', views.preAlgebra, name='Pre-Algebra'),

    # Physics
    path('physical-calculation', views.physicalCalculation, name='Physics'),
    path('physical-value-converter',views.physicalValueConverter, name='Physical-value-converter'),

    #Programming
    path('binary', views.binary, name='Binary'),
    path('sorting',views.sorting,name='Sorting'),

    #Algorithms
    path('operating-system-algorithms',views.osAlgorithms,name="osAlgorithms"),
    
    # path('countletters', views.countletters, name='Countletters'),
]
