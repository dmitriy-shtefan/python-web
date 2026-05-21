from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Course
from .models import Module
from .models import Enrollment


User = get_user_model()


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name', 'description', 'number_of_classes', 'order']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'is_test', 'price', 'modules']


# If EnrollmentSerializer does not need every field from CourseSerializer,
# we create a smaller serializer just for nested enrollment output
class CourseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    course = CourseShortSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'course', 'student']
