from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import Settings, settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))
]

urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)