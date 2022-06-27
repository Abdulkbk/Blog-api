from rest_framework.routers import SimpleRouter
from .views import LoginViewSet, RegistrationViewSet, RefreshViewSet, UserViewSet


routes = SimpleRouter()

routes.register(r'login', LoginViewSet, basename='auth-login')
routes.register(r'register', RegistrationViewSet, basename='auth-register')
routes.register(r'refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'users', UserViewSet, basename='users')

urlpatterns = [
  *routes.urls
]