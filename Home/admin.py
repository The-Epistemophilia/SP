from django.contrib import admin
from .models import home_page
from .models import about_me
from .models import my_resume
# Register your models here.

admin.site.register(home_page)
admin.site.register(about_me)
admin.site.register(my_resume)