from django.contrib import admin
from django.contrib.auth.models import User
from .models import District, Center, User_details, Slots
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
class UserDetailsInline(admin.StackedInline):
    model = User_details
    can_delete = False
    verbose_name_plural = 'User details'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDetailsInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Center)
admin.site.register(District)
admin.site.register(Slots)
