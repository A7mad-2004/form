from django.contrib import admin

from url_model.models import Cource, Parson, Student, User

# Register your models here.
admin.site.register(Parson)
admin.site.register(Cource)
admin.site.register(User)
admin.site.register(Student)
    
