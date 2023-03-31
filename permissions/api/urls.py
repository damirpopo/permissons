from django.urls import path
from .views import *

urlpatterns = [
    path('tour/', dawdawfaf.as_view()),
    path('tour/<int:pk>', TourUpdateDestroy.as_view()),
    path('country/', CountryList.as_view()),
    path('country/<int:pk>', CoyntryUpdateDestroy.as_view()),
    path('privcab/', PrivateCabinetListt.as_view()),
    path('privcab/<int:pk>', PrivateCabinetDestroyUpdate.as_view()),
    path('excursion/', Excursionlistt.as_view()),
    path('excursion/<int:pk>', ExcursionDestroyUpdate.as_view()),
]