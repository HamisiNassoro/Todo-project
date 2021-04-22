
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import Task, phoneModel, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','username','password','first_name','last_name','Mobile')



class phoneModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = phoneModel
        fields = '__all__'
