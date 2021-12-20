from django.urls import path
from . import views

app_name = 'CDLib'
urlpatterns = [
    path('report/', views.report, name='report'),
    path('detail<int:pk>/', views.DetailCD.as_view(), name='detail'),
    path('createCD/', views.CreateCD.as_view(), name='crtCD'),
    path('updateCD<int:pk>/', views.UpdateCD.as_view(), name='updCD'),
    path('deleteCD<int:pk>/', views.DeleteCD.as_view(), name='delCD'),

    path('createLib/', views.CreateLib.as_view(), name='crtLib'),
    path('updateLib<int:pk>/', views.UpdateLib.as_view(), name='updLib'),
    path('deleteLib<int:pk>/', views.DeleteLib.as_view(), name='delLib'),
]