from rest_framework import serializers
from .models import Service,Hostel,Excursions,Tour,Country,PrivateCabinet


class ExursionsSerializers(serializers.ModelSerializer):
    user= serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Excursions
        fields = '__all__'

class TourSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Tour
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Country
        fields = '__all__'

class PrivateCabSerializers(serializers.ModelSerializer):
    user= serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = PrivateCabinet
        fields = '__all__'