from django.urls import path, include
from .views import PostList, PostDetail, UserList, UserDetail


urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("users/", UserList.as_view()),  # new
    path("users/<int:pk>/", UserDetail.as_view()),  # new
    path("", PostList.as_view()),
    path("<int:pk>/", PostDetail.as_view()),
]
