from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flashcard_id>/check/', views.check_answer, name='check_answer'),
]