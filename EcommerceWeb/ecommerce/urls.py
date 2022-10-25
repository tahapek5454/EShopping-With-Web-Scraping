from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage,name='home'),
    path("home", views.homepage),
    path("<int:id>",views.prodDetails,name='productDetails'),
    path("descsort",views.DescSortProd,name="SortprodDesc"),
    path("ascsort",views.AscSortProd,name="SortprodAsc"),
    path("starsort",views.prodStarSort,name="SortprodStar"),
]