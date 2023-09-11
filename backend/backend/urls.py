from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('post.urls')),
    path('admin/', admin.site.urls),
    # Redirect '/' to 'api/v1/Home'
]
