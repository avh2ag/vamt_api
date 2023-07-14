from django.contrib import admin
from django.urls import path
from reference import urls as reference_urls
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ObtainTokenPairView

auth_urls = [
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls
urlpatterns += reference_urls.urlpatterns
