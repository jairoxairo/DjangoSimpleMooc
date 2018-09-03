from django.urls import path, include
from simplemooc.courses import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
]