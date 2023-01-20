from django.contrib import admin
from .models import *
from django.utils.timezone import now
from django.utils.html import format_html
# Register your models here.
admin.site.site_header='Khurshed Admin Panel'
admin.site.site_title='User Admin Panel'
admin.site.index_title=" "

class Comment_Inline(admin.TabularInline):
    model=Comment

class RecordAdmin(admin.ModelAdmin):
    #fields=('user','name')
   # exclude= ('staff_id',)
    readonly_fields=('slug',)
   # list_display=('user','name','email','amount','group','subject')
  
    list_display=('user','name','email','amount','category','medium','get_subjects','get_group','created_at','created_since','title_html_display')
    list_filter=('user','subject','group')
    search_fields=('address','user__username','subject__name','group__name','name','category')
    filter_horizontal=('subject','group')
    list_editable=('amount',)
    list_display_links=('user',)
    actions=('change_salary_30000',)
    inlines= [ Comment_Inline, ] 
             

    def change_salary_30000(self,request,queryset):
        count=queryset.update(amount=30000)
        self.message_user(request,'{} record updated'.format(count))
    change_salary_30000.short_description='ChangeSalary'

    def created_since(self,RecordModel):
        diff=now()- RecordModel.created_at
        return diff.days
        
    created_since.short_description='Since Created'  

    def title_html_display(self,obj):
        return format_html(f'<span style="font-size:20px;color:red;">{obj.name}</span>') 
    title_html_display.short_description='Title'

    def get_subjects(self,obj):
        return "," .join([p.name for p in obj.subject.all()])
    get_subjects.short_description="Subjects"

    def get_group(self,obj):
        return "," .join([p.name for p in obj.group.all()])
    get_group.short_description="Group"    

    



admin.site.register(GroupModel)
admin.site.register(SubjectModel)
admin.site.register(RecordModel,RecordAdmin)
admin.site.register(PostModel)
admin.site.register(Comment)

