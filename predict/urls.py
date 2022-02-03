from django.urls import path

from . import views

app_name = 'predict'
urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    # path('predicted_result/', views.predicted_result, name='predicted_result'),
]
