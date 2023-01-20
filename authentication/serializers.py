from rest_framework import serializers
from authentication.models import User, Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ("is_active", 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        
    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        instance.is_active = True

        if password is not None:
            instance.set_password(password)
        instance.save()
        
        print(instance.user_role)
        
        if instance.user_role == 'Student':
            student_instance = Student(**{'user_id': instance})
            student_instance.save()
        else:
            teacher_instance = Teacher(**{'user_id': instance})
            teacher_instance.save()
            
        
        return instance 
        

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'