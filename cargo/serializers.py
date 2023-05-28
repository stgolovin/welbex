from rest_framework import serializers
from .models import Cargo, Vehicle, Location

import random
from geopy import distance


class CargoSerializer(serializers.ModelSerializer):  
    vehicles_number = serializers.SerializerMethodField()
    class Meta:
        model = Cargo
        fields = ['pickuplocation', 'delieverylocation', 'weight', 'description', 'vehicles_number']

    def get_vehicles_number(self, obj):
        obj.pickuplocation
        vehicles = Vehicle.objects.all()
        counter = 0
        # считаем количество машин, которые ближе 450 миль к грузу
        for vehicle in vehicles:
            vehiclelocation = (vehicle.currentlocation.latitude, vehicle.currentlocation.longitude)
            cargolocation  = (obj.pickuplocation.latitude, obj.pickuplocation.longitude)
            ladistanzia =  f"{round(distance.distance(vehiclelocation, cargolocation).miles)}"
            if int(ladistanzia) <= 450:
                counter += 1
        return f"{counter}"
    

class RetrieveCargoSerializer(serializers.ModelSerializer):
    vehicles = serializers.SerializerMethodField()
    class Meta:
        model = Cargo
        fields = ['pickuplocation', 'delieverylocation', 'weight', 'description', 'vehicles']

    def get_vehicles(self, obj):
        obj.pickuplocation
        vehicles = Vehicle.objects.all()
        vehicles_list = list()
        # полоучаем список номеров машин и их расстояние до груза
        for vehicle in vehicles:
            vehiclelocation = (vehicle.currentlocation.latitude, vehicle.currentlocation.longitude)
            cargolocation  = (obj.pickuplocation.latitude, obj.pickuplocation.longitude)
            ladistanzia =  f"{round(distance.distance(vehiclelocation, cargolocation).miles)}"
            item = f"{vehicle.uuid}: {ladistanzia} miles"
            vehicles_list.append(item)
        return f"{vehicles_list}"


class CreateCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

    def to_internal_value(self, data):
        # получаем pickuplocation по введеному zip коду
        pickuplocation_zip = data['pickuplocation']
        pickuplocation = Location.objects.all().filter(zip=pickuplocation_zip)
        # получаем delieverylocation по введеному zip коду
        delieverylocation_zip = data['delieverylocation']
        delieverylocation = Location.objects.all().filter(zip=delieverylocation_zip)
        # получаем случайную weight
        weight = random.randint(1, 1000)
        # переписываем key/value в словаре      
        data['pickuplocation'] = pickuplocation[0].id        
        data['delieverylocation'] = delieverylocation[0].id
        data['weight'] = weight
        return super().to_internal_value(data)
    

class EditCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def to_internal_value(self, data):
        # получаем случайный uuid
        first = random.randint(0, 9)
        second = random.randint(0, 9)
        third = random.randint(0, 9)
        forth = random.randint(0, 9)
        fith = lambda x, y: chr(random.randint(ord(x), ord(y)))
        uuid = f"{first}{second}{third}{forth}{fith('A', 'Z')}"
        # получаем случайную currentlocation
        leng = len(Location.objects.all())
        random_id = random.randint(0, leng)
        currentlocation = Location.objects.all().filter(id=random_id)
        # получаем случайную loadcapacity
        loadcapacity = random.randint(1, 1000)
        # переписываем key/value в словаре        
        data['uuid'] = uuid  
        data['currentlocation'] = currentlocation[0].id     
        data['loadcapacity'] = loadcapacity   
        return super().to_internal_value(data)
    

class EditVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

