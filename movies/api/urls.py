from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet,MovieCreateAPIView,MovieUpdateAPIView,MovieDeleteAPIView

router = DefaultRouter()
router.register(r'', MovieViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('create',MovieCreateAPIView.as_view()),
    path('<pk>/update',MovieUpdateAPIView.as_view()),
    path('<pk>/delete',MovieDeleteAPIView.as_view()),
]
