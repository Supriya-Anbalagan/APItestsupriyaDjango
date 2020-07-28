from django.shortcuts import render
from rest_framework import viewsets
from.models import Register, Password, Deposit, Withdraw
from.serializers import RegisterSerializer, PasswordSerializer, DepositSerializer, WithdrawSerilizer
from rest_framework.response import Response

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = AssetSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
class PasswordViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = AssetSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
class DepositViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = AssetSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
class WithdrawViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('-id')
    serializer_class=AssetSerializer
    
    def create(self,request,*args,**kwargs):
        try:
            serialiser = AssetSerializer(data = request.data)
            serialiser.is_valid(raise_exception=True)
            serialiser.save()
            return Response(serialiser.data)
        except Exception as e:
            print('e--',e)
            
            
    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        instance.delete() 
