from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),
    path('api/auth/', include('user.urls'))
]
