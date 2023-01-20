from import_export import resources
from authentication.models import User, Teacher, Student
from courses.models import Course
from comments.models import Comment

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        
class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        
class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        
class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment