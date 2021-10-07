from django.contrib import admin
from .models import User,candidate_info,Blog,postajob,Message,Shortlist
# Register your models here.

admin.site.register(candidate_info)
admin.site.register(Blog)
admin.site.register(postajob)
admin.site.register(Message)
admin.site.register(Shortlist)
