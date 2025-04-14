from django.urls import path
from . import views


urlpatterns = [
path("create-table/", views.create_table, name="create_table_url"),
    path("pre-edit-table/<int:id>/", views.pre_edit_table, name="pre_edit_table_url"),
    path("edit-table/<int:id>/", views.edit_table, name="edit_table_url"),
    path("delete-table/<int:id>/", views.delete_table, name="delete_table_url"),
    path("", views.table, name="table_url"),
]