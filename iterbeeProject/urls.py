"""
URL configuration for iterbeeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from iterbeeBackend import views #gives error in pycharm for some reason

router = routers.DefaultRouter()
router.register(r'api', views.CulturalPointViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    #add authentification to access API I think this is
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
