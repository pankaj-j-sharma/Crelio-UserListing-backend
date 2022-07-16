"""crelio_api_framework URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views


urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/',include('rest_api.urls'))
]
