from courses.models import Course
from comments.models import Comment

from courses.serializers import CourseSerializer
from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q

from courses.forms import CourseForm


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
def index(request):
    search_query = request.GET.get('search')
    
    if search_query:
        try:
            courses = Course.objects.filter(Q(title__contains=search_query) | Q(description__contains=search_query))
            print(courses)
        except:
            courses = None
    else:
        courses = Course.objects.all()
        
    form = CourseForm()
    context = {'courses': courses, 'form': form}
    return render(request, 'courses/index.html', context)

def show(request, id):
    course = Course.objects.get(pk=id)
    reviews = Comment.objects.filter(course_id_id=id)
    context = {'course': course, 'reviews': reviews}
    
    return render(request, 'courses/show.html', context)

def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("courses:index")
            except Exception as e:
                print(e)
    else:
        form = CourseForm()
    
    courses = Course.objects.all()
    return render(request, 'courses/index.html', { 'form': form, 'courses': courses })
    
def edit(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm
    return render(request, 'courses/edit.html', { 'course': course, 'form': form  })

def update(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST, instance=course)
    if form.is_valid():
        form.save()
        return redirect("courses:show", id=id)
    
    return render(request, 'courses/edit.html', { 'course': course, 'form': form })

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')



            