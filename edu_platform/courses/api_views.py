from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CourseSerializer
from .models import Course


@api_view(['GET'])
def course_list_api(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)