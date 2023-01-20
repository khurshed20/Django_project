from django.contrib import admin
from Rest_Api.models import Company
from Rest_Api.models import Topic
from Rest_Api.models import Topic_Entry,Topic_Entry_comment
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
   list_display=( 'name','address','mail','mobile','about')#,'about')

admin.site.register(Company, CompanyAdmin )

class CommentsAdmin(admin.ModelAdmin):
   list_display=( 'text','id')#,'about')

admin.site.register(Topic)
admin.site.register(Topic_Entry)
admin.site.register(Topic_Entry_comment,CommentsAdmin)      