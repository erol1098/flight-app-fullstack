from rest_framework import routers

from flight.views import FlightView

router = routers.DefaultRouter()
router.register("flights", FlightView)

urlpatterns = [
    
]

urlpatterns += router.urls
