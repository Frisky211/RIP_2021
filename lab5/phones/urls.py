from django.urls import path
from . import views

app_name = 'phones'
urlpatterns = [
    path('', views.mainView, name='main'),
    path('phones/', views.PhonesView.as_view(), name='phonesList'),
    path('manufact/', views.ManufacView.as_view(), name='manufacList'),
    path('phones/<int:pk>/', views.PhoneDetail.as_view(), name='phonesDetail'),
    path('manufact/<int:pk>/', views.ManufacDetail.as_view(), name='manufacDetail'),
]
