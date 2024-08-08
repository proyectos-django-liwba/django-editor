from django.contrib import admin
from django.urls import path, include
from djgentelella.urls import urlpatterns as djgentelellaurls

urlpatterns = djgentelellaurls + [
    path('', include('src.draw.urls'), name='index'),
    path('panel/', include('src.panelApp.urls')),
    path('admin/', admin.site.urls),
]
