from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("<int:id>/",views.list,name="list"),
    path("deleteitem/<int:id>",views.delete_item,name="deleteitem"),
    path("deletelist/<int:id>",views.delete_list,name="deletelist"),
    path("update/<int:id>",views.update,name="update"),
]
