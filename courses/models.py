from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.

class Course(models.Model):
    title = models.CharField(verbose_name='Course title ', max_length=255)
    description = models.TextField(verbose_name='Course description')
    cost = models.IntegerField(verbose_name='Course price ', default=1)
    duration = models.IntegerField(verbose_name='Course duration in month ', default=1)

    history = HistoricalRecords()
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'