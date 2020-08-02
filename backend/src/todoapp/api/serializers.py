from rest_framework import serializers
from todoapp.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'content', 'is_done']
        model = Todo
