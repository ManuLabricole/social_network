from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/posts/', include('post.urls')),
    path('api/v1/users/', include('friendship.urls')),
    # Redirect '/' to 'api/v1/Home'
]
