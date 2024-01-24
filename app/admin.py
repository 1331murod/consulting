from django.contrib import admin

from.models import *

class UniversityImageAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(UniversityImage, UniversityImageAdmin)



class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']
    filter_horizontal = ['gallery']
    readonly_fields = ['video']

admin.site.register(University, UniversityAdmin)



class UniversityRequirementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

admin.site.register(UniversityRequirements, UniversityRequirementsAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'faculty', 'university']
    list_filter = ['faculty', 'university']
    search_fields = ['full_name', 'faculty']
    readonly_fields = ['student_info']
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'image')
        }),
        ('Academic Information', {
            'fields': ('faculty', 'university')
        }),
        ('Opinion', {
            'fields': ('opinion',)
        }),
        ('Additional Information', {
            'fields': ('student_info', 'video')
        })
    )

class OurAdvantagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

admin.site.register(Our_advantages, OurAdvantagesAdmin)



class FormAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number']
    search_fields = ['full_name', 'phone_number']
    

admin.site.register(Form, FormAdmin)