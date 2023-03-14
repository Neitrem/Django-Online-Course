from django.forms import fields
from courses.models import Course
from django import forms

from django.utils.translation import gettext_lazy as _


class CourseForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = "__all__"
        
        labels = {
            'title': _('Название'),
            'description': _('Описание'),
            'cost': _('Цена'),
            'duration': _('Продолжительность'),
        }
