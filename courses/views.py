from courses.models import Course
from courses.serializers import CourseSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Course

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
def courses_index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/index.html', context)