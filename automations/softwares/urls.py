from rest_framework.routers import DefaultRouter
from .views import (
  BetSiteViewset
)

router = DefaultRouter()
router.register(r'betsite',BetSiteViewset,basename="betsite")