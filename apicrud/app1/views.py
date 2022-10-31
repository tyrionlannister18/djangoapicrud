from functools import partial
from os import stat
from django.shortcuts import render
from .models import Student
from .serializers import StudentSer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.http import Htt
# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer = StudentSer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSer(stu,many=True)
        return Response(serializer.data)
 
 
    
    def post(self,request,format=None):
        serializer = StudentSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
 
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Complete data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        