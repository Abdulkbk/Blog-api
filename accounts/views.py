from django.views import View
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from accounts.models import CustomUser
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer

"""Class-based view"""
class LoginViewSet(ModelViewSet, TokenObtainPairView):
  serializer_class = LoginSerializer
  permission_classes = (AllowAny,)
  http_method_names = ['post']

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    
    if serializer.is_valid():
      return Response(serializer.validated_data, status=status.HTTP_200_OK)

    else:
      raise InvalidToken()




class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
  serializer_class = RegisterSerializer
  permission_classes = (AllowAny,)
  http_method_names = ['post']

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = { "refresh": str(refresh), "access": str(refresh.access_token) }

    return Response({
      "user": serializer.data,
      "refresh": res['refresh'],
      "token": res['access']
    }, status=status.HTTP_201_CREATED)



class RefreshViewSet(ViewSet, TokenRefreshView):
  permission_classes = (AllowAny,)
  http_method_names = ['post']

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    try:
      serializer.is_valid(raise_exception=True)
    except TokenError as e:
      raise InvalidToken(e.args[0])

    return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
  http_method_names = ['get']
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)

  def get_queryset(self):
    if self.request.user.is_superuser:
      return CustomUser.objects.all()

  def get_object(self):
    lookup_field_value = self.kwargs[self.lookup_field]

    obj = CustomUser.objects.get(lookup_field_value)
    self.check_object_permissions(self.request, obj)

    return obj