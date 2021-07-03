from django.urls import path

from . import views

app_name = 'bookreviewer'

urlpatterns = [
    path('', views.review_list, name='review_list'),
]
