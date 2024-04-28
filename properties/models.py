from django.db import models


class Property(models.Model):
    city = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.property_type} in {self.city}"


class Property(models.Model):
    BUY = 'buy'
    RENT = 'rent'
    HOUSE = 'house'
    APARTMENT = 'apartment'
    TYPE_CHOICES = [
        (BUY, 'Buy'),
        (RENT, 'Rent'),
    ]
    CATEGORY_CHOICES = [
        (HOUSE, 'House'),
        (APARTMENT, 'Apartment'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=BUY)
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default=HOUSE)
    city = models.CharField(max_length=100)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    max_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    square_feet = models.IntegerField()
    fully_equipped = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    microwave = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address}, {self.city} - {self.category}"


class HotDeal(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    deal_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Hot Deal on {self.property.address} - ${self.deal_price}"
