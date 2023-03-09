from courses.models import Course
from comments.models import Comment

from courses.serializers import CourseSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Course

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/index.html', context)

def show(request, id):
    course = Course.objects.get(pk=id)
    comments = Comment.objects.filter(course_id_id=id)
    context = {'course': course, 'comments': comments}
    
    return render(request, 'courses/show.html', context)