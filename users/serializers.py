# Serializers define the API representation.
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = User(
            username=validated_data.get('username', None),
            first_name=validated_data.get('first_name',None),
            last_name=validated_data.get('last_name',None)
        )
        user.set_password(validated_data.get('password', None))
        user.save()
        return user

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'id', 'username',
                  'first_name', 'last_name','password',
                  'is_superuser', 'is_staff','is_active')


        extra_kwargs = {
            'url': {
                'view_name': 'users:user-detail',
            }
        }
