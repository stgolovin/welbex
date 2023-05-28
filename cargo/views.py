# Импортируем необходимые модули
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Импортируем модели и сериализаторы из нашего приложения cargo
from cargo.models import Cargo, Vehicle, Location
from cargo.serializers import CargoSerializer, RetrieveCargoSerializer, CreateCargoSerializer, EditCargoSerializer, VehicleSerializer, EditVehicleSerializer, LocationSerializer

# Создаем классы ViewSet для каждой модели
class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['weight', ]


class RetrieveCargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = RetrieveCargoSerializer


class CreateCargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CreateCargoSerializer


class EditCargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = EditCargoSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class EditVehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = EditVehicleSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer