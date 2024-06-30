from django.contrib import admin
from .models import InitialConfig, UsabilityTutorials, UsageTips, Maintenance, Support

admin.site.register(InitialConfig)
admin.site.register(UsabilityTutorials)
admin.site.register(UsageTips)
admin.site.register(Maintenance)
admin.site.register(Support)
