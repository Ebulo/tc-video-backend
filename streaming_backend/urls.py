from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from vdo_api.routers.userRouters import router as userRouter
from vdo_api.routers.videoRouters import videoRouter

# Use of an FTP Server is preferable here

urlpatterns = [
    path('', include(userRouter.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(videoRouter.urls)),
]


urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
