from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
  
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/list/', views.CarListApiView.as_view(), name='car-list'),
    path('api/detail/<int:pk>/', views.CarDetailApiView.as_view(), name='detail'),
    path('api/create/', views.CarCreateApiView.as_view(), name='create'),
    path('api/update/<int:pk>/', views.CarUpdateApiView.as_view(), name='update'),
    path('api/delete/<int:pk>/', views.CarDeleteApiView.as_view(), name='delete'),
]
