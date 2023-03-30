from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

# from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Go to /api/v1/")


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


"""
    (generic views in Django REST framework)

    1- ListAPIView for a read only list endpoint
    2- RetrieveAPIView for a read only single endpoint details view which is the traditional in Django
    3- ListCreateAPIView for a read and write list endpoint
    4- RetrieveUpdateDestroyAPIView for a read and write single endpoint details view

"""


"""
    Token Authentication in Django REST framework
    
    once the client send a request a unique token is generated 
    for that client and it is stored in cookie or local Storage

"""
