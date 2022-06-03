from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import Profile

Desc = 'Add College Email-ID'
class UserAdminConfig(UserAdmin):
    model = Profile
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('username','email', 'first_name', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)
    list_display = ('username','email', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        ('Section 1', {'fields': ('email', 'first_name', 'last_name',),  
                       'description': '%s' % Desc,
        
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active'),
                         'classes': ('collapse',),
        }),
       
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

class Admin(admin.AdminSite):
    site_header = 'MPT'

# admin.site.unregister(User)

admin_site = Admin(name='MPTAdmin')
admin_site.register(Profile, UserAdminConfig)
