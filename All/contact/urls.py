"""Ecomerce URL Configuration

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
from news import views as album_vies


urlpatterns = [
    path('contacts', contact_views.ContactList.as_view(), name='contact_list'),
    path('contact/<int:pk>', contact_views.ContactDetail.as_view(), name='contact_detail'),
    path('create', contact_views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', contact_views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', contact_views.ContactDelete.as_view(), name='contact_delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








