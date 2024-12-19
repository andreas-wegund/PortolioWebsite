### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
from django.contrib.auth.models import User
from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice

from utils.abstracts.abstract_models.abstract_model import AbstractModel





### ============================================================================================ #
### UserProfile
### ============================================================================================ #
class UserProfile( AbstractModel, models.Model ):
      user = models.OneToOneField( User, unique=True, blank=False, on_delete=models.CASCADE )
      profilepic = models.ImageField( upload_to='profilepics/', default='_default_profilepic.png', max_length=100, blank=False )
      otp_device = models.OneToOneField( TOTPDevice, unique=True, blank=True, null=True, on_delete=models.CASCADE )
      
      
      ### ------------------------------------------------- #
      ### META CLASS
      ### ------------------------------------------------- #
      class Meta:
            verbose_name = 'User Profile'
            verbose_name_plural = 'User Profiles'
      
      
      ### ------------------------------------------------- #
      ### METHODS
      ### ------------------------------------------------- #
      def __str__( self ):
            return f"{self.user.first_name} {self.user.last_name}"
