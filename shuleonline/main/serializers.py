from rest_framework import serializers
from main.models import Student, Teacher, Material, Assignment, Choice, Question, Ancwer, Score, Mission
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import User


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AncwerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ancwer
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    # darasa = serializers.PrimaryKeyRelatedField(read_only=True)
    # darasa = Circular(many=False)

    # def create(self, validated_data):
    #     return Assignment.objects.create(**validated_data)

    class Meta:
        model = Assignment
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    # def create(self, validated_data):
    #     def create(self, validated_data):
    #         return Student.objects.create(**validated_data)


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model: Material
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    # question = AssignmentSerializer('question', many=False)

    # def create(self, validated_data):
    #     return Choice.objects.create(**validated_data)

    class Meta:
        model = Choice
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

    # def create(self, validated_data):
    #     darasa_data = validated_data.pop('darasa')
    #     subject_data = validated_data.pop('subjects')
    #     darasa = Darasa.objects.create(**darasa_data)
    #     subject = Subject.objects.create(**subject_data)
    #     teacher = Teacher.objects.create(subjects=subject,
    #                                      darasa=darasa, **validated_data)
    #     return teacher
