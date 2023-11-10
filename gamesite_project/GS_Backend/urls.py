from django.urls import include, path
from rest_framework import routers
from GS_Backend import views

router = routers.DefaultRouter()
router.register(r'leaderboard', views.LBEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]