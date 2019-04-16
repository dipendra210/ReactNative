from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from .models import Brand, Post, Model, UserRequest, Profile
from rest_framework.response import Response

from authy.api import AuthyApiClient

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ['user', 'phonenumber', 'authy_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(user=user, phonenumber=validated_data.pop('phonenumber'), authy_id=validated_data.pop('authy_id'))

        # email = validated_data['email']
        # username = validated_data['username']
        # password = '1'
        # phonenumber = validated_data['phonenumber']

        # if ( User.objects.filter( email = email ).exists() ):
        #     raise serializers.ValidationError('email already exists')

        # new_user = User(username=username, email=email)
        # new_user.set_password(password)
        
        # new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return profile

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    class Meta:
        model = Model
        fields = ['id', 'name', 'category']

class UserRequestSerializer(serializers.ModelSerializer):
    user  = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())
    
    class Meta:
        model = UserRequest
        fields = ['user', 'brand', 'model', 'year_from', 'year_to', 'price_start', 'price_end', 'trans_gear', 'kilo_from', 'kilo_to']

class PostSerializer4Create(serializers.ModelSerializer):
    user  = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())

    class Meta:
        model = Post
        fields = ['user', 'brand', 'model', 'year_of_made', 'price_is_hidden', 'is_freezed', 'convertable', 'viewers', 'posted_on', 'transmission', 'price', 'Kilometer', 'sunroof', 'description', 'contact', 'whatsApp', 'email', 'img0', 'img1', 'img2', 'img3', 'img4', 'img5', 'img6' ]

class PostSerializer4Special(serializers.ModelSerializer):
    user  = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    model = serializers.PrimaryKeyRelatedField(queryset=Model.objects.all())

    class Meta:
        model = Post
        fields = ['user', 'brand', 'model', 'year_of_made', 'price_is_hidden', 'is_freezed', 'convertable', 'viewers', 'posted_on', 'img0', 'img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'transmission', 'price', 'Kilometer', 'sunroof', 'description', 'contact', 'whatsApp', 'email', 'is_special', 'first_owner','is_from_kwait', 'is_under_warranty', 'is_get_accident', 'is_repainted', 'condition', 'is_accept_exam', 'mini_price', 'has_visible_defect', 'comment', 'communication']


class PostSerializer(serializers.ModelSerializer):
    user  = UserSerializer(read_only=True)
    brand = CarBrandSerializer(read_only=True)
    model = CarModelSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'  