from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .serializers import CourseSerializer

from .models import Course


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def course_list_api(request):
    if request.method == 'GET':
        courses = Course.objects.filter(is_test=False).prefetch_related('modules')
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        course = serializer.save()
        result_serializer = CourseSerializer(course)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)