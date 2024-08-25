from django.db import models
from django.core.validators import MaxValueValidator as mxvv
from django.contrib.auth import get_user_model


User = get_user_model()


class Journey(models.Model):
    place = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    tourist = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='journey')

    def __str__(self):
        return self.place


class Blog(models.Model):
    JOURNEY_CATEG = (
        ('citybreaks', 'City breaks'),
        ('corporate', 'Corporate'),
        ('cultural', 'Cultural'),
        ('general', 'General'),
        ('holidays', 'Holidays'),
    )
    journey = models.ForeignKey(Journey,
                                on_delete=models.CASCADE,
                                related_name='blog')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=100,
                                choices=JOURNEY_CATEG)
    image = models.ImageField(upload_to='blog',
                              blank=True,
                              null=True)
    ratings = models.PositiveSmallIntegerField(default=1,
                                               validators=[mxvv(5)])

    def __str__(self):
        return f"{self.name} in {self.journey.place}"
