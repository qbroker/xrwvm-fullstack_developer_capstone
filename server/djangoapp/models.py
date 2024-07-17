from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# from django.utils.timezone import now // removed after linting
# Register the models in djangoapp admin.py
# Car Make model


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation

# Car Make has many Car Models, Many-To-One relationship to Car Make model
# using ForeignKey field
# - Name
# - Type (CharField for choices arguments such as Sedan, SUV, WAGON)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon')
        # ('TRUCK', 'Truck') # Add one for testing
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                               ])

    # Other fields as needed
    # dealer_id = models.IntegerField()

    def __str__(self):
        return self.name  # Return the name as the string representation
