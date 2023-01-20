from authentication.views import UserViewSet, TeacherViewSet, StudentViewSet
from comments.views import CommentsRecordsView
from courses.views import CourseViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('comments', CommentsRecordsView)
