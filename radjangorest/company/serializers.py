from rest_framework import serializers
from .models import company
from .models import Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ['id', 'name', 'address', 'city', 'state', 'country', 'website', 'phone_number']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'