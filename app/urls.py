from django.urls import include, path
from rest_framework import routers
#from . import views
from .views import ShopViewSet
router=routers.DefaultRouter()
router.register(r'shops',ShopViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
