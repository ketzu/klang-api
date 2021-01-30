from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets, throttling
from rest_framework.decorators import action
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsSelf
from users.serializers import UserSerializer, GroupSerializer, EmailSerializer


class PasswordReset(APIView):
    permission_classes = [permissions.AllowAny]
    throttle_classes = [throttling.ScopedRateThrottle]
    throttle_scope = 'pwreset'

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            users = User.objects.filter(email=serializer['email'])
            if len(users) > 1:
                pass
            elif len(users) == 1:
                users[0]
            else:
                pass


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsSelf]

    def get_permissions(self):
        if self.request.method in ['POST', 'OPTIONS']:
            return [permissions.AllowAny()]
        return [IsSelf()]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
