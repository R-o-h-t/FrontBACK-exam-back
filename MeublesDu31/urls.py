"""MeublesDu31 URL Configuration

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
from django.urls import include, path
from backend.views import FurnitureViewSet, StoreViewSet, ManagerViewSet, FurnitureAPIViewPostStatus
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'furnitures', FurnitureViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'managers', ManagerViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    # post on /api/furnitures/status/{id}
    path(r'furnitures/status/<int:id>',
         FurnitureAPIViewPostStatus.as_view()),
    path(r'admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
