from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("<int:id>/", views.postDetail, name="post"),
    # set the url to home page
    path("", views.redirectToHome),
]
