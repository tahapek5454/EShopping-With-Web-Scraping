from django.urls import path
# path gostermemizi saglayan kutuphabe
from . import views


# urlpatterns icine uygulanamanın yonlenecegi url leri belirtiriz
urlpatterns = [
    path("", views.home),
    path("<int:id>", views.productDetail), # detail da simdilik her pc ozgu id gelsin olarak dusunelim
]