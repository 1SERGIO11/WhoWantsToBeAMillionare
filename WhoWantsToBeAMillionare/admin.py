from django.contrib import admin
from .models import User, Questions, Hint

admin.site.register(User)
admin.site.register(Questions)
admin.site.register(Hint)
