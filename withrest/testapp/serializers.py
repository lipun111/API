from rest_framework import serializers
from testapp.models import Employee

def multiple_of_1000(value):
    if value %1000 != 0:
        raise serializers.ValidationError("Salary shoud be Multiple of 1000")
    return value

class EmployeeSerializers(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiple_of_1000])
    class Meta:
        model = Employee
        fields ="__all__"
# class EmployeeSerializers(serializers.Serializer):
#     eno = serializers.IntegerField()
#     ename = serializers.CharField(max_length=60)
#     esal = serializers.FloatField(validators=[multiple_of_1000])
#     eaddr = serializers.CharField(max_length=100)
#
#     def validate_esal(self, value):
#         if value<5000:
#             raise serializers.ValidationError('Salary shoud be graterthan 5000')
#         return value
#
#     def validate(self, data):
#         ename = data.get('ename')
#         esal = data.get('esal')
#         if ename.lower() == 'sunny':
#             if esal<50000:
#                 raise serializers.ValidationError('Sunny Salary must be graterthan 50000')
#         return data
#
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.eno = validated_data.get('eno', instance.eno)
#         instance.ename = validated_data.get('ename', instance.ename)
#         instance.esal = validated_data.get('esal', instance.esal)
#         instance.eaddr = validated_data.get('eaddr', instance.eaddr)
#         instance.save()
#         return instance
