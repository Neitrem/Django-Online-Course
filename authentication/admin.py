from django.contrib import admin
from authentication.models import User
from authentication.models import Student
from authentication.models import Teacher
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_role', 'age', 'email') 
        

class UserAdminView( UserAdmin):
    list_display = ('id','email', 'last_login','first_name','user_role', 'password',)
    list_display_links = ('id','email','first_name')
    search_fields = ('id', 'email','user_role',)
    list_editable = ('user_role',)
    list_filter = ('user_role', 'last_login')

class UserAdmin( ImportExportModelAdmin):
    resource_class = UserResource
    
    
    list_display = ('id','email', 'last_login','first_name','user_role', 'password',)
    list_display_links = ('id','email','first_name')
    search_fields = ('id', 'email','user_role',)
    # list_editable = ('user_role',)
    list_filter = ('user_role', 'last_login')


from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User



admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)