from rest_framework import generics
from .serializers import TodoSerializer
from todoapp.models import Todo

class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer