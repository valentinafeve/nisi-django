"""nisi URL Configuration

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
from django.contrib import admin
from django.urls import path
from app_feed import views as feed_views
from app_map import views as map_views
from app_network import views as net_views
from app_nuser import views as nuser_views

urlpatterns = [

    path('admin/', admin.site.urls),
    # Feed
    path('fd/twfollowings/', feed_views.tw_followings),
    path('fd/fbfollowings/', feed_views.fb_followings),
    path('fd/igfollowings/', feed_views.ig_followings),
    path('fd/notifications/', feed_views.notifications),
    # Map
    path('map/nearusers/', map_views.near_users),
    path('map/updatelocation/', map_views.update_location),
    # Net
    path('net/follow/', net_views.follow),
    path('net/rate/', net_views.rate),
    path('net/profile/', net_views.profile),
    # Nisi user
    path('nu/profile/', nuser_views.profile),
    path('nu/signup/', nuser_views.signup),
    path('nu/signin/', nuser_views.signin),
    path('nu/settings/', nuser_views.settings),
    path('nu/updatesetting/', nuser_views.update_setting),
    path('nu/addsn/', nuser_views.add_sn),
]
