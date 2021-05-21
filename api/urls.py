from django.urls import include, path
from django.views.generic import TemplateView

from .routers import v1_router
from .views import MyTokenObtainPairView

urlpatterns = [
    path(
        'auth/token/',
        MyTokenObtainPairView.as_view(),
        name='my_token_obtain_pair'
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('v1/', include(v1_router.urls)),
]
