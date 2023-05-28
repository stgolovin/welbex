# Импортируем необходимые модули и классы.
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from cargo.views import CargoViewSet, RetrieveCargoViewSet, CreateCargoViewSet, EditCargoViewSet, VehicleViewSet, EditVehicleViewSet, LocationViewSet

# Создаем экземпляр класса DefaultRouter.
router = DefaultRouter()
# Регистрируем наши ViewSet'ы на различных URL'ах.
router.register('cargo', CargoViewSet)
router.register('retrivecargo', RetrieveCargoViewSet)
router.register('createcargo', CreateCargoViewSet)
router.register('editcargo', EditCargoViewSet)
router.register('vehicles', VehicleViewSet)
router.register('editvehicles', EditVehicleViewSet)
router.register('locations', LocationViewSet)


# Создаем список urlpatterns, который содержит путь к административной панели Django и URL'ы, зарегистрированные в нашем DefaultRouter'е.
urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
