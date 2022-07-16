import email
from tkinter import CASCADE
import uuid
from django.db import models
from django.forms.models import model_to_dict
from datetime import datetime
from django.utils.timezone import now

# model_to_dict convert the model output to dict format



class UserLogin(models.Model):
    id =  models.UUIDField(primary_key=True)
    username = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    pwd_text = models.CharField(max_length=500)
    pwd_md5 = models.CharField(max_length=100)
    pwd_sha = models.CharField(max_length=100)
    pwd_sha256 = models.CharField(max_length=100)

    class Meta:
        db_table = "user_login"



class UserIdModel(models.Model):
    userid = models.ForeignKey(UserLogin, on_delete=models.CASCADE )
    class Meta:
        abstract = True


class UserInfo(UserIdModel):
    title = models.CharField(max_length=10)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=10)
    dob = models.DateField()
    age = models.IntegerField(default=0)
    reg_date = models.DateField(default=now)
    profile_l = models.URLField()
    profile_m = models.URLField()
    profile_t = models.URLField()

    class Meta:
        db_table = "user_info"



class UserContact(UserIdModel):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cell = models.CharField(max_length=20)

    class Meta:
        db_table = "user_contact"



class UserLocation(UserIdModel):
    street_name = models.CharField(max_length=200)
    street_no = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)
    coordinates_lat = models.FloatField()
    coordinates_long = models.FloatField()
    timezone_offset = models.CharField(max_length=100)
    timezone_desc = models.CharField(max_length=200)

    class Meta:
        db_table = "user_location"

