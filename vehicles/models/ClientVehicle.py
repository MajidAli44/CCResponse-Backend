from .AbstractVehicle import AbstractVehicle


class ClientVehicle(AbstractVehicle):
    class Meta:
        verbose_name = 'Client vehicle'
        verbose_name_plural = 'Client vehicles'
