from django.urls import path
from cinema import views

urlpatterns = [
    path("movies/", views.movie_list),
    path("movie/<int:pk>/", views.movie_detail),
]
