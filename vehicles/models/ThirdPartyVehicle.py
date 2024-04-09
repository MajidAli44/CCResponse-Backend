from .AbstractVehicle import AbstractVehicle


class ThirdPartyVehicle(AbstractVehicle):
    class Meta:
        verbose_name = 'Third party vehicle'
        verbose_name_plural = 'Third party vehicles'
