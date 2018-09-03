from django.contrib import admin
from .models import Course
# Register your models here.

#essa classe customiza o admin, adiciona esses campos ao admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    #preenche os atalhos com o nome que esta sendo digitado
    prepopulated_fields = {'slug': ('name',)}
#registra o courses no admin
admin.site.register(Course, CourseAdmin)