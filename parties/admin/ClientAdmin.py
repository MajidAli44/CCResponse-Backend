from django.contrib import admin

from parties.models import Client, Introducer


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Introducer)
class IntroducerAdmin(admin.ModelAdmin):
    pass