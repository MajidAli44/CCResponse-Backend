from django.urls import path
from rest_framework import routers

from parties.views import InsurerViewSet, SolicitorViewSet, IntroducerViewSet, ProviderViewSet, ExtraPartyCountAPIView

router = routers.SimpleRouter()

router.register(r'insurers', InsurerViewSet, basename='insurers')
router.register(r'solicitors', SolicitorViewSet, basename='solicitors')
router.register(r'introducers', IntroducerViewSet, basename='introducers')
router.register(r'providers', ProviderViewSet, basename='providers')

urlpatterns = [
    path('extra_party_counts/', ExtraPartyCountAPIView.as_view(),
         name='extra_party_counts'),
]

urlpatterns += router.urls
