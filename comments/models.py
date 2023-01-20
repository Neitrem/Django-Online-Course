from django.db import models
from simple_history.models import HistoricalRecords
from courses.models import Course
from authentication.models import User

# Create your models here.

class Comment(models.Model):
    text = models.TextField(verbose_name='Comment text')
    course_id = models.ForeignKey(verbose_name='Course id ', to=Course, on_delete=models.CASCADE)
    
    user_id = models.ForeignKey(verbose_name='User id ', to=User, on_delete=models.CASCADE, blank=True)
    
    history = HistoricalRecords()
    def __str__(self):
        return self.user_id.pk
    
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'