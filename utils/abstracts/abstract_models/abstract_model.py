### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
### ============================================================================================ #
### DJANGO EXTENSIONS
### ============================================================================================ #
from django_extensions.db.models import (
      TimeStampedModel,
      ActivatorModel,
)





### ============================================================================================ #
### CLASS USER MODEL
### ============================================================================================ #
class AbstractModel( TimeStampedModel, ActivatorModel, models.Model ):
      """
      We use this for EVERY DB as the baseline
      """
      id = models.UUIDField( _( "id" ), primary_key=True, unique=True, default=uuid.uuid4 )
      
      
      class Meta:
            abstract = True
            ordering = [ "created" ]
