from django.urls import path
from . import views

app_name = 'technobaza'
urlpatterns = [
    path('', views.ListView.as_view(), name='master'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('report/', views.reportView, name='report')
]
