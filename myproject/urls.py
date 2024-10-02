from django.contrib import admin
from django.urls import path, include

from products.views import LoginAuthView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("products.urls")),
    path("api/v1/login/", LoginAuthView.as_view(), name='token_obtain_pair'),
    path('api/v1/register/', RegisterView.as_view(), name='register'),
]
