from django.contrib import admin
from .models import Guesthouse,Rooms,Reservation,Contact

# Register your models here.
admin.site.register(Guesthouse)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Contact)