### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
from django.contrib import admin

from .models import UserProfile





### ============================================================================================ #
###  Admin Console: Display & Filter Options
### ============================================================================================ #
class AdminUserProfile( admin.ModelAdmin ):
      list_display = [ 'id', 'user__username', 'user__first_name', 'user__last_name', 'user__is_active', 'user__date_joined', 'user__is_staff', 'user__is_superuser', 'otp_device__name' ]
      list_filter = list_display
      ordering = [ 'user__last_name' ]
      search_fields = [ 'user__username', 'user__email', 'user__first_name', 'user__last_name', 'user__is_active', 'user__date_joined' ]
      date_hierarchy = 'user__date_joined'





### ============================================================================================ #
###  Admin Console: Class Registration
### ============================================================================================ #
admin.register( UserProfile )
