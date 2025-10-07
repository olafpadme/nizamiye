from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_data, name="create_data"),
    path("edit/<int:pk>/", views.edit_data, name="edit_data"),
    path("delete/<int:pk>/", views.delete_data, name="delete_data"),
    path("list/", views.list_data, name="list_data"),
    path("cikis/", views.cikis, name="cikis"),
    path("", views.index, name="index")

]
