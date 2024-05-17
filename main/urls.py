from django.urls import path, include
from main.views import main



urlpatterns = [path("main/", main, name="main")]