### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
from .base_settings import *



load_dotenv()

### ============================================================================================ #
### INTERNAL_IPS
### ============================================================================================ #
INTERNAL_IPS = [
      '127.0.0.1',
      'localhost',
]

### ============================================================================================ #
### ALLOWED_HOSTS & CSRF_TRUSTED_ORIGINS
### ============================================================================================ #
ALLOWED_HOSTS = os.environ[ "DJANGO_ALLOWED_HOSTS_" + DJANGO_RUN_MODE ].split( ' ' )
# CROSS SITE REQUEST FORGERY
CSRF_TRUSTED_ORIGINS = os.environ[ 'CSRF_TRUSTED_ORIGINS_' + DJANGO_RUN_MODE ].split( ' ' )

### ============================================================================================ #
### MEDIA FILES & CLOUDINARY STORAGE
### ============================================================================================ #
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# STATIC_URL -> prefix for the urls in the templates where staticfiles are stored in Development
STATIC_URL = '/static/'
# STATICFILES_DIRS -> in Development django will try to search here for existing staticfiles
# Should match the above folders, accordingly
STATICFILES_DIRS = [
      os.path.join( BASE_DIR, 'static' ),
      os.path.join( BASE_DIR, 'media' ),
]
# *_ROOT -> this is where the `pyhton manage.py collectstatic` command will store the files for
#           Deployment to Production ( so this should be `staticFILES` & `mediaFILES`
STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )  # -->
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
MEDIA_URL = '/media/'  # or any prefix you choose

### ============================================================================================ #
### EMAIL SETTINGS
### ============================================================================================ #
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
