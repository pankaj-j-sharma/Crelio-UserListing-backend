from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import generics
import requests
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import UserDetailsSerializer,UserListDataSerializer
from .models import UserContact, UserInfo, UserLocation, UserLogin
from .parser import parse_api_data
from rest_framework import filters

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from django.core.cache import cache,caches

class AllUserDataView(generics.ListAPIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )  
    queryset =  UserLogin.objects.prefetch_related('userinfo_set').all().order_by('id')
    serializer_class = UserListDataSerializer

    # @method_decorator(cache_page(60*60*1),'alldataview')
    # @method_decorator(vary_on_headers("Authorization"))
    def dispatch(self, *args, **kwargs):
        return super(AllUserDataView, self).dispatch(*args, **kwargs)


class UserDetailDataView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, )  
    queryset =  UserLogin.objects.prefetch_related('userinfo_set','usercontact_set','userlocation_set').all().order_by('id')
    serializer_class = UserDetailsSerializer    

    # @method_decorator(cache_page(60*60*2))
    # @method_decorator(vary_on_headers("Authorization",))
    def dispatch(self, *args, **kwargs):
        return super(UserDetailDataView, self).dispatch(*args, **kwargs)


class SearchUserView(generics.ListAPIView,PageNumberPagination):
    queryset =  UserLogin.objects.prefetch_related('userinfo_set').all().order_by('id')
    serializer_class = UserListDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','^username','userinfo__first','userinfo__last','=userinfo__gender']

    # @method_decorator(cache_page(60*60*2))
    # @method_decorator(vary_on_headers("Authorization",))
    def dispatch(self, *args, **kwargs):
        return super(SearchUserView, self).dispatch(*args, **kwargs)


class LoadExternalDataView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = (IsAuthenticated, )  
    
    def post(self, request, format=None):
        result={}
        records = min(int(self.request.data.get('records',2)),5000)
        
        # as per documentation Random User Generator allows us to 
        # fetch up to 5,000 generated users in one request using the results parameter
        resp = requests.get(f'https://randomuser.me/api/?results={records}')
        resp_status = resp.status_code
        if resp_status == 200:
            data = resp.json()
            output = parse_api_data(data)

            UserLogin.objects.bulk_create(output['UserLogin'])
            UserInfo.objects.bulk_create(output['UserInfo'])
            UserContact.objects.bulk_create(output['UserContact'])
            UserLocation.objects.bulk_create(output['UserLocation'])
            
            result['total_users'] = UserLogin.objects.count()
            result['status'] = resp_status
            result['message'] = 'Data for {noofrecords} users loaded successfully'.format(noofrecords=len(output['UserLogin']))
            # invalidating cache on successful load 
            cache.clear()
        else:
            result['status'] = resp_status
            result['message'] = 'error'
        return Response(result)