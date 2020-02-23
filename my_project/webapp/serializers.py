from rest_framework import serializers
from webapp.models import Template


class TemplateSerializers(serializers.Serializer):
    # class Meta:
    #     model = Template
    #     fields = '__all__'

    template_name = serializers.CharField(max_length=100)
    delimeter = serializers.CharField(max_length=100)
    encode = serializers.CharField(max_length=100)
    catagory = serializers.CharField(max_length=100)
    sub_catagory = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Template.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.template_name = validated_data.get('template_name', instance.template_name)
        instance.delimeter = validated_data.get('delimeter', instance.delimeter)
        instance.encode = validated_data.get('encode', instance.encode)
        instance.catagory = validated_data.get('catagory', instance.catagory)
        instance.sub_catagory = validated_data.get('sub_catagory', instance.sub_catagory)
        instance.save()
        return instance




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
