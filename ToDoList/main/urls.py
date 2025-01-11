from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("<int:id>/",views.list,name="list"),
    path("delete/<int:id>",views.delete,name="delete"),
]
