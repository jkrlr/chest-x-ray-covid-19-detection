from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('team/', views.team, name='team'),
]
