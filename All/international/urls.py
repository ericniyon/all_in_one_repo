"""international URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from profiles import views as profiles_views
from contact import views as contact_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profiles_views.ListPost.as_view(), name='home'),
    path('about/', profiles_views.about, name='about'),
    path('profile/', profiles_views.userProfile, name='profile'),
    path('<slug:slug>/', profiles_views.PostDetails.as_view(), name='post_detail'),
    path('contact/', contact_views.contact, name='contact'),
    path('movue/', include('news.urls')),
    path('pay/', include('payroll.urls')),
    path('cont/', include('contact.urls')),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)