from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
    path('<uuid:user_id>/posts/', include('post.urls')),
]
