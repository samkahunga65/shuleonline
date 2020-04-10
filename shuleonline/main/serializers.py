from rest_framework import serializers
from main.models import Student, Teacher, Subject, Darasa, Material
from phonenumber_field.modelfields import PhoneNumberField


class SubjectSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Subject
        fields = ['subject']


class Circular(serializers.ModelSerializer):
    class Meta:
        model = Darasa
        fields = ['darasa']

    def create(self, validated_data):
        darasa = Darasa.objects.create(**validated_data)
        return darasa


class TeacherCircular(serializers.ModelSerializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number = serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = Circular('darasa', many=False)
    # darasa = DarasaSerializer(many=False)
    subjects = SubjectSerializer(many=False)

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    class Meta:
        model = Teacher
        fields = ['id',
                  'fname', 'lname', 'phone_number',
                  'age', 'darasa', 'subjects']
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            }}


class StudentCircular(serializers.ModelSerializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number = serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = Circular(many=False)

    class Meta:
        model = Student
        fields = ['id', 'fname', 'lname', 'phone_number',
                  'age', 'darasa']
        extra_kwargs = {
            "id": {
                "read_only": True,
                "required": False,
            }}

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        return student


# student serializer


class Circular(serializers.ModelSerializer):
    class Meta:
        model = Darasa
        fields = ['darasa']


class StudentSerializer(serializers.ModelSerializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number = serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = Circular(many=False)

    class Meta:
        model = Student
        fields = ['id', 'fname', 'lname', 'phone_number',
                  'age', 'darasa']
        extra_kwargs = {
            "id": {
                "read_only": True,
                "required": False,
            }}

    def create(self, validated_data):
        Darasa_data = validated_data.pop('darasa')
        darasa = Darasa.objects.create(**Darasa_data)
        student = Student.objects.create(darasa=darasa, **validated_data)
        return student


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model: Material
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    fname = serializers.CharField(max_length=20)
    lname = serializers.CharField(max_length=20)
    phone_number = serializers.CharField()
    age = serializers.IntegerField(default=0)
    darasa = Circular('darasa', many=False)
    # darasa = DarasaSerializer(many=False)
    subjects = SubjectSerializer(many=False)

    class Meta:
        model = Teacher
        fields = ['id',
                  'fname', 'lname', 'phone_number',
                  'age', 'darasa', 'subjects']
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            }}

    def create(self, validated_data):
        darasa_data = validated_data.pop('darasa')
        subject_data = validated_data.pop('subjects')
        darasa = Darasa.objects.create(**darasa_data)
        subject = Subject.objects.create(**subject_data)
        # darasa_serializer = Circular(data=darasa_data['darasa'])
        # darasa_serializer.is_valid()
        # darasa = darasa_serializer.save()

        # subject_serializer = SubjectSerializer(data=subject_data)
        # subject_serializer.is_valid()
        # subject = subject_serializer.save()
        teacher = Teacher.objects.create(subjects=subject,
                                         darasa=darasa, **validated_data)
        return teacher


class DarasaStudentSerializer(serializers.ModelSerializer):
    darasa = serializers.CharField(max_length=30)
    darasa_student = StudentSerializer(many=True)

    class Meta:
        model = Darasa
        fields = ['darasa', 'darasa_student']

    def create(self, validated_data):
        student_data = validated_data.pop('darasa_student')
        print(student_data)
        darasas = Darasa.objects.create(**validated_data)
        for each in student_data:
            Student.objects.create(darasa=darasas, **each)
        return darasas

    def update(self, instance, validated_data):
        instance.darasa = validated_data.get('darasa', instance.darasa)
        instance.save()
        return instance

        if instance:
            instance.darasa = attrs.get('darasa', instance.darasa)
            return instance
        return Darasa(**attrs)


class DarasaSerializer(serializers.ModelSerializer):
    darasa = serializers.CharField(max_length=30)
    darasa_student = StudentSerializer(many=True)
    darasa_teacher = TeacherSerializer(many=True)

    class Meta:
        model = Darasa
        fields = ['darasa', 'darasa_student', 'darasa_teacher']

    def create(self, validated_data):
        student_data = validated_data.pop('darasa_student')
        teacher_data = validated_data.pop('darasa_teacher')
        darasa = Darasa.objects.create(**validated_data)
        for each in student_data:
            Student.objects.create(darasa=darasas, **each)
        for each in teacher_data:
            Teacher.objects.create(darasa=darasas, **each)
        return darasa

    def update(self, instance, validated_data):
        instance.darasa = validated_data.get('darasa', instance.darasa)
        instance.save()
        return instance

        if instance:
            instance.darasa = attrs.get('darasa', instance.darasa)
            return instance
        return Darasa(**attrs)
