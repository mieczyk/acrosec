from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('<int:flashcard_id>/check/', views.check_answer, name='check_answer'),
]