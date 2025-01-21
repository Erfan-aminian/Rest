from cgitb import reset
from rest_framework import routers
from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns =[
    path('register/', views.UserRegister.as_view(), name='register'),
    #path('api-token-auth/',auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSer)
urlpatterns += router.urls



# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNzU3MjA4MywiaWF0IjoxNzM3NDg1NjgzLCJqdGkiOiJlMjVhOTk0NzVlZTI0ZmUyOTE4M2IxODcyYTg4MDg3YSIsInVzZXJfaWQiOjF9.QVP4Jk3V0ePkAAF--3nwCMdgY5TuiofQawZlYb41Emg",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM3NDg1OTgzLCJpYXQiOjE3Mzc0ODU2ODMsImp0aSI6IjM0NDcxNjE4M2ZjYTQwMzRiMGRlYjgwZDNkMDBjYjBkIiwidXNlcl9pZCI6MX0.ZGRQjlwNaa1q5YqBxV7M70BEjcj_jZn6jJqCOeMKprI"
# }