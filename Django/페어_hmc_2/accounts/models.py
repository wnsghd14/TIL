from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

ge = (
    (1, "Male"),
    (2, "Female"),
)


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    usertall = models.IntegerField(default=0)
    userweights = models.IntegerField(default=0)
    userfat = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    user_sm = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    gender = MultiSelectField(choices=ge, max_choices=1)
    tier = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
