from django.contrib import admin
from django.urls import path, include
from djgentelella.urls import urlpatterns as djgentelellaurls

urlpatterns = djgentelellaurls + [
    path('', include('draw.urls'), name='index'),
    path('panel/', include('panelApp.urls')),
    path('admin/', admin.site.urls),
]
