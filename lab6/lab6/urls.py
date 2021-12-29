from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from lab_api import views as phone_views

router = routers.DefaultRouter()
router.register(r'phones', phone_views.PhoneViewSet)
router.register(r'manufacturers', phone_views.ManufacturerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
