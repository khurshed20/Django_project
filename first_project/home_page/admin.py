from django.contrib import admin
from home_page.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
   list_display=( 'student_name','student_class','student_email')

admin.site.register(Student, StudentAdmin )