from django.contrib import admin
from django.urls import path, include

from vdo_api.routers.userRouters import router as userRouter
from vdo_api.routers.videoRouters import videoRouter

urlpatterns = [
    path('', include(userRouter.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(videoRouter.urls)),
]
