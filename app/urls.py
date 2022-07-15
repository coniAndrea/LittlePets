from django.urls import path, include
from .views import home, login, registro, alimento, servicios, agregar_producto, \
     listar_producto, modificar_producto, eliminar_producto, \
     ProductoViewset, MarcaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('alimento/', alimento, name="alimento"),
    path('servicios/', servicios, name="servicios"),
    path('agregar_producto/',agregar_producto, name="agregar_producto"),
    path('listar_producto/',listar_producto, name="listar_producto"),
    path('modificar_producto/<id>/',modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('api/', include(router.urls)),
]