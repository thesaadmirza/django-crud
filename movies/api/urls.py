from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet,MovieCreateAPIView

router = DefaultRouter()
router.register(r'', MovieViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('create',MovieCreateAPIView.as_view()),
]
