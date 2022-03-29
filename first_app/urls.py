from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'firstobj', views.FirstObjViewSet)

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
