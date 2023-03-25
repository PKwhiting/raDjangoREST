from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.http import Http404


def home(request):
    return render(request, 'company/output.html')

class CompanyEmployeesList(APIView):
    def get(self, request, company_id):
        employees = Employee.objects.filter(company_id=company_id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class CompanyList(generics.ListCreateAPIView):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

    #Read
    def get(self, request):
        companies = company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    
    #Create
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

class CompanyAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class EmployeeList(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeDetail(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)