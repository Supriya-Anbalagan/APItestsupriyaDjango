from django.db import models
class Register(models.Model):
 username=models.charField(max_length=20)
 atm_pin=models.CharField(max_length=4)
 usercard= models.CharField(max_length=8)

class password(models.Model):
 atm_pin=models.CharField(max_length=4)
 usercard= models.CharField(max_length=8)

class Deposit(models.Model):
 accountname=models.CharField(max_length= 25)
 accountnumber= models.IntegerField(max_length=10)
 Money_to_deposit= models.IntegerField
 Register= models.Foreignkey(Register, on_delete=models.CASCADE)

class Withdraw(models.Model):
 accountname=models.CharField(max_length= 25)
 accountnumber= models.IntegerField(max_length=10)
 Money_to_withdraw = models.IntegerField
 Register= models.Foreignkey(Register, on_delete=models.CASCADE)

