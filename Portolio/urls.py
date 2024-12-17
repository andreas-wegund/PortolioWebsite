"""
URL configuration for Portolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
### ============================================================================================ #
### IMPORTS
### ============================================================================================ #
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users import views
from users.sitemaps import StatisticSitemap, CategorySitemap, PostPagesSitemap



### ============================================================================================ #
### SITEMAPS
### ============================================================================================ #

sitemaps = {
      'static':     StatisticSitemap,
      'categories': CategorySitemap,
      'posts':      PostPagesSitemap
}

### ============================================================================================ #
### URL-ROUTING
### ============================================================================================ #
urlpatterns = [
      
      # # Django creates the XML-file automatically
      # path( 'sitemap.xml', sitemap, { 'sitemaps': sitemaps }, name='django.contrib.sitemaps.view.sitemap' ),
      # robots.txt --> search engines should NOT index these pages
      path( 'robots.txt', TemplateView.as_view( template_name='robots.txt', content_type='text/plain' ) ),
      
      # path( 'admin/', admin.site.urls ),
      path( 'admin/', include( 'admin_honeypot.urls', namespace='admin_honeypot' ) ),
      path( 'aswc_admin/', admin.site.urls ),
      
      path( '', views.home, name='home' ),

]

### ============================================================================================ #
### STATICFILES & MEDIAFILES
### ============================================================================================ #
urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
