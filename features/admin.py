### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
from django.contrib import admin

from .models import Feature





### ============================================================================================ #
###  Admin Console: Display & Filter Options
### ============================================================================================ #
class AdminFeatures( admin.ModelAdmin ):
      list_display = [ 'developer', 'feature_name', 'image', 'staging_enabled', 'production_enabled', 'created' ]
      search_fields = list_display
      ordering = [ 'feature_name' ]
      date_hierarchy = 'created'





### ============================================================================================ #
###  Admin Console: Class Registration
### ============================================================================================ #
admin.register( Feature )
