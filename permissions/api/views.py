from django.shortcuts import render
from .models import Service, Hostel, Excursions, PrivateCabinet, Country, Tour
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TourSerializers, PrivateCabSerializers, ExursionsSerializers, CountrySerializers


class dawdawfaf(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

class TourUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Tour
    authentication_classes = (TokenAuthentication,)
    serializer_class = TourSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CountryList(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = CountrySerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class CoyntryUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Country
    serializer_class = CountrySerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class PrivateCabinetListt(ListAPIView):
    queryset = PrivateCabinet.objects.all()
    serializer_class = PrivateCabSerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class PrivateCabinetDestroyUpdate(RetrieveUpdateDestroyAPIView):
    queryset = PrivateCabinet
    serializer_class = PrivateCabSerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class Excursionlistt(ListAPIView):
    queryset = Excursions.objects.all()
    serializer_class = ExursionsSerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

class ExcursionDestroyUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Excursions
    serializer_class = ExursionsSerializers
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)

