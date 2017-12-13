from django.contrib import admin
from .models import Worker, Card, Reader, Record, Messages

admin.site.register(Worker)
admin.site.register(Card)
admin.site.register(Reader)
admin.site.register(Record)
admin.site.register(Messages)

# Register your models here.
