from django.db import models

class Emp(models.Model):
    Name_of_the_school=models.CharField(max_length=30)
    Regno=models.CharField(max_length=30)
    Board=models.CharField(max_length=25)
    Location=models.CharField(max_length=45)
    City=models.CharField(max_length=20)
    Pin=models.IntegerField()
    State=models.CharField(max_length=20)
    School_email=models.EmailField()
    Mobile_no=models.IntegerField()
    Mobile_no1=models.IntegerField()
    Land_line=models.IntegerField()
    Land_line1=models.IntegerField()
    Password=models.CharField(max_length=20)
    Con_password=models.CharField(max_length=20)
