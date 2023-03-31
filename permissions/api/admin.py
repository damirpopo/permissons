from django.contrib import admin
from .models import Service,Hostel,Excursions,PrivateCabinet,Country,Tour

admin.site.register(Tour)
admin.site.register(Country)
admin.site.register(PrivateCabinet)
admin.site.register(Excursions)
admin.site.register(Hostel)
admin.site.register(Service)
