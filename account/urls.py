from . import views

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
