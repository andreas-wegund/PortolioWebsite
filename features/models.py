### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
from django.db import models

from users.models import UserProfile
from utils.abstracts.abstract_models.abstract_model import AbstractModel





### ============================================================================================ #
### FEATURES
### ============================================================================================ #
class Feature( AbstractModel, models.Model ):
      developer = models.ForeignKey( UserProfile, blank=True, null=True, on_delete=models.CASCADE )
      feature_name = models.CharField( max_length=255, unique=True )
      image = models.ImageField( upload_to='features/', default='_default_feature.png', max_length=100, blank=False )
      staging_enabled = models.BooleanField( default=False )
      production_enabled = models.BooleanField( default=False )
      
      
      ### ------------------------------------------------- #
      ### META CLASS
      ### ------------------------------------------------- #
      # class Meta( AbstractModel.Meta ):
      class Meta:
            verbose_name = 'Feature'
            verbose_name_plural = 'Features'
      
      
      ### ------------------------------------------------- #
      ### METHODS
      ### ------------------------------------------------- #
      def __str__( self ):
            return self.feature_name
