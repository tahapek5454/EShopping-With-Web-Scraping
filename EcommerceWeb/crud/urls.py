from django.urls import path
from . import views


urlpatterns = [
    path("add", views.addProduct, name="addProduct"),
    path("update/<int:id>", views.updateProduct, name="updateProduct"),
    path("delete", views.deleteProduct, name="deleteProduct")
]