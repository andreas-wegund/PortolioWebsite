### ============================================================================================ #
###  IMPORTS
### ============================================================================================ #
from django.views.generic.base import TemplateView

from .models import UserProfile



### ------------------------------------------------- #
### APP_NAME
### ------------------------------------------------- #
app_name = 'users'





### ============================================================================================ #
### CLASS VIEWS: HOME
### ============================================================================================ #
class HomeView( TemplateView ):
      template_name = 'users/home.html'
      
      
      
      ### ------------------------------------------------- #
      ### META CLASS
      ### ------------------------------------------------- #
      def get_context_data( self, **kwargs ):
            context = super().get_context_data( **kwargs )
            userprofiles = UserProfile.objects.all()
            context[ 'userprofiles' ] = userprofiles
            return context





### ============================================================================================ #
### CLASS VIEWS: ABOUT
### ============================================================================================ #
class AboutView( TemplateView ):
      template_name = 'users/about.html'
      
      
      
      ### ------------------------------------------------- #
      ### META CLASS
      ### ------------------------------------------------- #
      def get_context_data( self, **kwargs ):
            context = super().get_context_data( **kwargs )
            userprofiles = UserProfile.objects.all()
            context[ 'userprofiles' ] = userprofiles
            return context





### ============================================================================================ #
### CLASS VIEWS: ABOUT
### ============================================================================================ #
class ContactView( TemplateView ):
      template_name = 'users/contact.html'
      
      
      
      ### ------------------------------------------------- #
      ### META CLASS
      ### ------------------------------------------------- #
      def get_context_data( self, **kwargs ):
            context = super().get_context_data( **kwargs )
            userprofiles = UserProfile.objects.all()
            context[ 'userprofiles' ] = userprofiles
            return context




# ### ============================================================================================ #
# ### VIEW FUNCTIONS / MODELS
# ### ============================================================================================ #
# # Create your views here.
# def home( request ):
#       # feature_Hero = False
#       # try:
#       #       feature_Hero = feature_enabled( request, 'HeroButton' )
#       # except:
#       #       feature_Hero = False
#       #
#       context = {
#             # 'fullname': f"{request.user.first_name} {request.user.last_name}",
#             # 'feature_HeroButton': feature_Hero,
#       }
#       #
#       # # send a mail using GMAIL
#       # if (settings.DJANGO_RUN_MODE == 'STAGING') | (settings.DJANGO_RUN_MODE == 'PRODUCTION'):
#       #       subject = settings.ACCOUNT_EMAIL_SUBJECT_PREFIX
#       #       message = 'Thank you for creating an account!'
#       #       from_email = settings.DEFAULT_FROM_EMAIL
#       #       recipient_list = [ 'andreas.wegund@omv.com' ]
#       #       mail_result = send_mail( subject, message, from_email, recipient_list )
#       #       # It will return 1 if the message was sent successfully, otherwise 0.
#
#       return render( request, 'users/home.html', { } )
