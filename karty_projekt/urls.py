"""karty_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from timework.views import reg_entrence, get_users, reg_card, get_messages, get_last_status, get_l_messages, main, user_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register_entrence/$', reg_entrence),
    url(r'^register_card/$', reg_card),
    url(r'^get_users/$', get_users),
    url(r'^get_mess/$', get_messages),
    url(r'^get_l_mess/$', get_l_messages),
    url(r'^get_ls/$', get_last_status),
    url(r'^home/$', main, name='main'),
    url(r'^user/$', user_detail, name='userdetails'),

]
