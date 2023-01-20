from django.contrib import admin
from data_analysis.models import Student01
from data_analysis.models import FileUploadModel

# Register your models here.


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
   list_display=( 'student_name','student_class','student_roll','student_email')

admin.site.register(Student01, StudentAdmin )
admin.site.register(FileUploadModel )