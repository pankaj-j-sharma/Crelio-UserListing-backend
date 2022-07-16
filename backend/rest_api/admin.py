from django.contrib import admin
from .models import UserLogin,UserInfo,UserContact,UserLocation

admin.site.register(UserLogin)
admin.site.register(UserInfo)
admin.site.register(UserContact)
admin.site.register(UserLocation)

