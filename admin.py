from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Equipment)
admin.site.register(Rental)
admin.site.register(FloorPlanRequirement)
admin.site.register(Worker)
admin.site.register(Job)
admin.site.register(JobAssignment)
admin.site.register(Shift)
admin.site.register(ShiftAssignment)