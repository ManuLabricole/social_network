from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/posts/', include('post.urls')),
    path('api/v1/friendship/', include('friendship.urls')),
    # Redirect '/' to 'api/v1/Home'
]
