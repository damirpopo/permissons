from django.db import models


class Country(models.Model):
    name=models.CharField(max_length=90,verbose_name='название')
    language=models.CharField(max_length=90,verbose_name='Язык')

    def __str__(self):
        return self.name

class Excursions(models.Model):
    name=models.CharField(max_length=90,verbose_name='название')
    place=models.CharField(max_length=90,verbose_name='место поездки')
    time=models.TimeField(verbose_name='время поездки')
    price=models.IntegerField(verbose_name='стоимость')

    def __str__(self):
        return self.name


class PrivateCabinet(models.Model):
    tours=models.CharField(max_length=90,verbose_name='тур')
    time=models.TimeField(verbose_name='время поездки')
    price=models.IntegerField(verbose_name='стоимость')

    def __str__(self):
        return self.tours

class Service(models.Model):
    sevice=models.CharField(max_length=20,verbose_name='Сервис')

    def __str__(self):
        return self.sevice

class Hostel(models.Model):
    stars=models.CharField(max_length=20,verbose_name='скольки звёздная гостиница')

    def __str__(self):
        return self.stars


class Tour(models.Model):
    name=models.ForeignKey(PrivateCabinet,on_delete=models.CASCADE,verbose_name='Название тура')
    country=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name='Название страны')
    time=models.DateTimeField(verbose_name='Время прохождения')
    service=models.ForeignKey(Service,on_delete=models.CASCADE,verbose_name='Сервис')
    countHuman=models.IntegerField(verbose_name='количество человек')
    hostel=models.ForeignKey(Hostel,verbose_name='Гостиница',on_delete=models.CASCADE)
    excursions=models.ForeignKey(Excursions,on_delete=models.CASCADE,verbose_name='экскурсии')
    price=models.IntegerField(verbose_name='цена тура+экскурсии')





