from django.contrib import admin
from django.http.request import HttpRequest

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
admin.site.register(Student,StudentAdmin)

class OurAdvantagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

admin.site.register(Our_advantages, OurAdvantagesAdmin)



class FormAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number']
    search_fields = ['first_name', 'phone_number']
    

admin.site.register(Form, FormAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



admin.site.register(Gallery)


class ourResultsAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset


    def has_add_permission(self, request: HttpRequest) -> bool:
        return our_results.objects.count() < 4
admin.site.register(our_results, ourResultsAdmin)
