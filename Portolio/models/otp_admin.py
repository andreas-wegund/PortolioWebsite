### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
from django.contrib.auth.models import User
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice

from features.admin import AdminFeatures
from features.models import Feature
# User
from users.admin import AdminUserProfile
from users.models import UserProfile





### ============================================================================================ #
### OTP CLASS
### ============================================================================================ #
class OTPAdmin( OTPAdminSite ):
      list_display = [ 'id', 'username', 'email', 'is_active', 'created' ]





### ============================================================================================ #
### ADMIN CONSOLE: REGISTER MODELS
### ============================================================================================ #
admin_site = OTPAdmin( name='OTPAdmin' )
admin_site.register( TOTPDevice )

# User
admin_site.register( User )

# Custom Models
admin_site.register( UserProfile, AdminUserProfile )
admin_site.register( Feature, AdminFeatures )
