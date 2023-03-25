from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    #Read
    def get(self, request):
        companies = User.objects.all()
        serializer = UserSerializer(companies, many=True)
        return Response(serializer.data)
    
    #Create
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



#class UserListCreateAPIView(generics.ListCreateAPIView):
 #   queryset = User.objects.all()
  #  serializer_class = UserSerializer
   # permission_classes = [permissions.AllowAny]

#class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
 #   queryset = User.objects.all()
  #  serializer_class = UserSerializer
