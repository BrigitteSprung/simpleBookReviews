from django.urls import path

from . import views

app_name = 'bookreviewer'

urlpatterns = [
    path('', views.review_list, name='list'),
    path('create/', views.review_create, name='create'),
    path('<id>', views.review_detail, name='detail'),
    path('<id>/update/', views.review_update, name='update'),
    path('<id>/delete/', views.review_delete, name='delete'),

]
