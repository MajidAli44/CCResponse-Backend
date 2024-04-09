from .AbstractExternalParty import AbstractExternalParty


class Provider(AbstractExternalParty):
    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'
