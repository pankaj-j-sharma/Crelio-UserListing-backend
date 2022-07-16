from pyexpat import model
import json
from rest_framework import serializers
from .models import UserLogin,UserInfo,UserContact,UserLocation

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','username','salt','pwd_text']
        read_only_fields = fields


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['title','first','last','gender','nationality','dob','age','reg_date','profile_l','profile_m','profile_t']
        read_only_fields = fields


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = ['email','phone','cell']
        read_only_fields = fields


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ['street_name','street_no','city','state','country','postcode','coordinates_lat','coordinates_long','timezone_offset','timezone_desc']
        read_only_fields = fields


class UserDetailsSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = UserLogin
        fields=['id','username','salt','pwd_text','pwd_md5','pwd_sha','info','contact','location']
        read_only_fields = fields

    def get_info(self,obj):
        # qs_info = UserInfo.objects.filter(userid=obj)  
        qs_info = obj.userinfo_set
        return UserInfoSerializer(qs_info,many=True).data

    def get_contact(self,obj):
        # qs_contact = UserContact.objects.filter(userid=obj)  
        qs_contact = obj.usercontact_set
        return UserContactSerializer(qs_contact,many=True).data

    def get_location(self,obj):
        # qs_location = UserLocation.objects.filter(userid=obj)  
        qs_location = obj.userlocation_set
        return UserLocationSerializer(qs_location,many=True).data


class UserInfoShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['first','last','gender','dob']
        read_only_fields = fields


class UserListDataSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = UserLogin
        fields=['id','username','info']
        read_only_fields = fields

    def get_info(self,obj):
        qs_info = obj.userinfo_set
        return UserInfoShortSerializer(qs_info,many=True).data
   