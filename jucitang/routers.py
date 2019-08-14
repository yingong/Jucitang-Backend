from django.urls import path, include
from rest_framework import routers
from items.views import ItemView
router = routers.DefaultRouter()
router.register('items', ItemView, base_name='items')
urlpatterns = router.urls
