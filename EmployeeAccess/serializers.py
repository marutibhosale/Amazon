
from rest_framework import serializers
from .models import Employee, Access          # import  Employee table from model.py file (database)


class EmployeeSerializer(serializers.ModelSerializer):  # use ModelSerializer
    class Meta:
        model = Employee
        fields = '__all__'                               # take all fields


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

