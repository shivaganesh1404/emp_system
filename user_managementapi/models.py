from django.db import models


class UserProfile(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=9)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    profile_picture = models.CharField(max_length=1000)

