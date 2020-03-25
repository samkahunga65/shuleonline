from rest_framework import serializers
from main.models import Student, Teacher, Subject, Darasa, Material
from phonenumber_field.modelfields import PhoneNumberField


#student serializer
class StudentSerializer(serializers.Serializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number =  serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = serializers.PrimaryKeyRelatedField(queryset=Darasa.objects.all())
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'phone_number', 'age', 'darasa']

class TeacherSerializer(serializers.Serializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number =  serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = serializers.PrimaryKeyRelatedField(queryset=Darasa.objects.all())
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = Teacher
        fields = ['fname', 'lname', 'phone_number', 'age', 'darasa', 'subjects']
    

class DarasaSerializer(serializers.Serializer):
    darasa = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Darasa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.darasa = validated_data.get('darasa', instance.darasa)
        instance.save()
        return instance

        if instance:
            instance.darasa = attrs.get('darasa', instance.darasa)
            return instance
        return Darasa(**attrs)

class SubjectSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=30)
    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.subject = validated_data.get('subject', instance.subject)
        instance.save()
        return instance

        if instance:
            instance.subject = attrs.get('subject', instance.subject)
            return instance
        return Subject(**attrs)

class MaterialSerializer(serializers.Serializer):
    
    class Meta:
        model: Material
        fields = '__all__'


