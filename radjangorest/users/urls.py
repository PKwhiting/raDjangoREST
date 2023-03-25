from django.urls import path
from users.views import UserList, UserAPIView

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserAPIView.as_view(), name='user-detail'),
]
