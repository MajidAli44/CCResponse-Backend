from django.urls import path, include

from vehicles.views import (
    VehicleListCreateAPIView, VehicleRetrieveUpdateDestroyAPIView,
    VehicleBookingsAPIView, ExpenseListCreateAPIView,
    ExpenseUpdateDestroyAPIView, VehicleFieldsDefaultPriceAPIView,
)

urlpatterns = [
    path('', VehicleListCreateAPIView.as_view(), name='vehicle_create'),
    path('<int:pk>/', include([
        path('', VehicleRetrieveUpdateDestroyAPIView.as_view(),
             name='vehicle_retrieve_update_destroy'),
        path('bookings/', VehicleBookingsAPIView.as_view(),
             name='vehicle_bookings'),
        path('expenses/', ExpenseListCreateAPIView.as_view(),
             name='vehicle_expenses_list'),
        path('expenses/<int:pk>/', ExpenseUpdateDestroyAPIView.as_view(),
             name='vehicle_expenses_update_delete'),
    ])),
    path('default_prices/', VehicleFieldsDefaultPriceAPIView.as_view(),
         name='vehicle_default_prices')
]
