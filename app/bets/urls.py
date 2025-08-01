from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('update_shotguns_owed/<int:player_id>/', views.update_shotguns_owed, name='update_shotguns_owed'),
]