from rest_framework import serializers
from.models import Register, Password, Deposit, withdraw
class RegisterSerializer(serializers.ModelSerializer):
 class Meta:
  model= Register
  fields='__all__'
class PasswordSerializer(serializers.ModelSerializer):
 class Meta:
  model= Password
  fields='__all__'
class DepositSerializer(serializers.ModelSerializer):
 class Meta:
  model= Deposit
  fields='__all__'
class WithdrawSerializer(serializers.ModelSerializer):
 class Meta:
  model= Withdraw
  fields='__all__'