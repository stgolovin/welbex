from django.contrib import admin
from cargo.models import Cargo, Vehicle, Location

admin.site.register(Cargo)
admin.site.register(Vehicle)
admin.site.register(Location)