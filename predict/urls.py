from django.urls import path

from . import views

app_name = 'predict'
urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('predict_result/', views.predict_result, name='predict_result'),
]
