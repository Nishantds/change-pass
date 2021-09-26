# from django.urls import path,include

from userapp.api import views
from rest_framework.routers import DefaultRouter




# router.register('crud',views.UserViewSet,basename='user')

# urlpatterns=[
#     path('',include(router.urls)),
#     path('auth/',include('rest_framework.urls',namespace='rest_framework'))
# ]
from .views import RegisterAPI
from django.urls import path,include
from knox import views as knox_views
from .views import LoginAPI,UserViewSet,ChangePasswordView


router=DefaultRouter()
router.register('crud',views.UserViewSet,basename='user')
urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    # path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('login/', LoginAPI.as_view(), name='login'),
    # path('crud/', UserViewSet.as_view(), name='user'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]