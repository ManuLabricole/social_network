from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # Using 'id' as the lookup field
    # If you're using a different field name like 'uuid', make sure to change this
