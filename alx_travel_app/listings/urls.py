from django.urls import path, include
from rest_framework import routers
from .views import ListingView, BookingView, PaymentView

router = routers.DefaultRouter()
router.register(r"listings", ListingView, basename="listing")
router.register(r"bookings", BookingView, basename="booking")
router.register(r"payment", PaymentView, basename="payment")

urlpatterns = [
    path("", include(router.urls)),
]