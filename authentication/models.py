from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from simple_history.models import HistoricalRecords

from courses.models import Course

from web_project.validators import correct_string_length, correct_age_value
from authentication.manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    TEACHER = 'Teacher'
    STUDENT = "Student"
    ROLE_CHOICES = [
        (TEACHER ,'Teacher'),
        (STUDENT,'Student'),
    ]
    
    email = models.EmailField(verbose_name='User email ', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First name ', max_length=255)
    last_name = models.CharField(verbose_name='Last name ', max_length=255)
    age = models.IntegerField(verbose_name='User age ', blank=True, null=True)
    user_role = models.CharField(verbose_name='User role ', max_length=255, 
                                choices=ROLE_CHOICES, default=STUDENT, null=True)
    
    is_active = models.BooleanField(verbose_name='Is active', default=False)
    is_staff = models.BooleanField(verbose_name='Is staff', default=False, blank=True)
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)
    
    objects = UserManager()
    
    
    history = HistoricalRecords()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self) -> str:
        return str(self.email)
    
    def clean(self):
        correct_string_length(self.first_name, 4)
        correct_string_length(self.last_name, 5)
        correct_age_value(self.age, 16)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id', 'email']
    

class Student(models.Model):
    user_id = models.OneToOneField(verbose_name='User email ', 
                                    to=User, primary_key=True, on_delete=models.CASCADE)
    
    courses_id = models.ManyToManyField(verbose_name='User courses ',
                                    to = Course, related_name = 'user_courses', blank=True)
    
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.user_id.email)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
class Teacher(models.Model):
    user_id = models.OneToOneField(verbose_name='User email ', 
                                    to=User, primary_key=True, on_delete=models.CASCADE)
    
    courses_id = models.ManyToManyField(verbose_name='Teacher courses ', 
                                    to = Course, related_name = 'teacher_courses', blank=True)
    
    work_age = models.IntegerField(verbose_name='Techer work age ',  null=True)
    
    history = HistoricalRecords()
    
    def __str__(self):
        return str(self.user_id.email)
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
