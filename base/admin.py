from django.contrib import admin

from .models import Menu, SpTvr, SpGrp, SpOrg, Doc, Tvr, Prov

# Register your models here.

admin.site.register(Menu)
admin.site.register(SpTvr)
admin.site.register(SpGrp)
admin.site.register(SpOrg)
admin.site.register(Doc)
admin.site.register(Tvr)
admin.site.register(Prov)


