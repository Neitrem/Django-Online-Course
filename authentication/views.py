from authentication.models import User, Teacher, Student
from authentication.serializers import UserSerializer, TeacherSerializer, StudentSerializer


from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # def list(self, reauest):
    #     users = User.objects.all()
    #     user_serialised = UserSerializer(users, )
    #     return Response(user_serialised.data)
    
    @action(methods=['POST'], detail=False, url_path='registration')
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'msg': 'Registred successfully', 'user': serializer.data})
    
    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'введите почту'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'придумайте пароль'})

        try: 
            user = User.objects.get(email=request.data['email'])    
        except User.DoesNotExist:
            raise NotFound({'error': 'пользователь не найден'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'неверный пароль'})

        if not user.is_active:
            raise AuthenticationFailed({'error': 'подтвердите на почте'})    

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response
    
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated], url_path='account')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)
    
    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated], url_path='logout')
    def logout(self, request):
        response = Response()
        response.delete_cookie('refresh')
        return response
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAdminUser], url_path='role')
    def get_by_role(self, request):
        role_to_filter = request.GET.get('role')
        users = User.objects.filter(Q(user_role__icontains=role_to_filter))
        user_serialized = UserSerializer(users, many=True)
        return Response({'amount': len(user_serialized.data), 'data': user_serialized.data})
    
    
   
      
    
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    
    @action(methods=['POST'], detail=False, permission_classes=[IsAdminUser], url_path='set_to_course')
    def set_to_course(self, request):
        teacher = request.teacher
        
    
    
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
