from django.urls import path
# path gostermemizi saglayan kutuphabe
from . import views


# urlpatterns icine uygulanamanın yonlenecegi url leri belirtiriz
urlpatterns = [
    path("", views.home, name='home'),
    path("<int:id>", views.productDetails, name='productDetails'), # detail da simdilik her pc ozgu id gelsin olarak dusunelim
]