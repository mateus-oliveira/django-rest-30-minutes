from django.contrib import admin
from django.urls import path, include

from apirest.routes import router

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
