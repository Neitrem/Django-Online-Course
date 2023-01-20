from django.contrib import admin
from comments.models import Comment
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'last_login','first_name','user_role', 'password',)
    list_display_links = ('id','email','first_name')
    search_fields = ('id', 'email','user_role',)
    list_editable = ('user_role',)
    list_filter = ('user_role', 'last_login')

admin.site.register(Comment)