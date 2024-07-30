from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('', include('draw.urls'), name='index'),
    path('panel/', include('panelApp.urls'), name='panel'),
    path('admin/', admin.site.urls),
]
