from rest_framework.routers import DefaultRouter
from .views import (
  BetSiteViewset,
  BetSiteDesktopViewset
)

router = DefaultRouter()
router.register(r'betsite',BetSiteViewset,basename="betsite")
router.register(r'betsite-desktop',BetSiteDesktopViewset,basename="betsite-desktop")
