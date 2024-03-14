from django.db import models

# Create your models here.


class userdetails(models.Model):
    SI_NO=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    roll=models.IntegerField(max_length=100)
    
    class Meta:
        db_table='Userinfo'

class contactdetails(models.Model):
    si_no=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    query=models.CharField(max_length=500)
    
    class Meta:
        db_table='User_Contact_details'