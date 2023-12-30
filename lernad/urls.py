from django.urls import path, include
from . import views
urlpatterns = [
  path("",views.IndexView,name="index"),
  path("form/",views.Forms,name="Forms"),
]