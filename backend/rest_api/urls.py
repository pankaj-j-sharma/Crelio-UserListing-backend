from django.urls import path
from .views import LoadExternalDataView,AllUserDataView,SearchUserView, UserDetailDataView

urlpatterns=[
    path('loaddata/',LoadExternalDataView.as_view()),
    path('search/',SearchUserView.as_view()),
    path('detail/<uuid:pk>',UserDetailDataView.as_view()),
    path('',AllUserDataView.as_view())    
]



