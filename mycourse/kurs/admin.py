from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Course)
class MovieAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Faculty)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Room)
admin.site.register(Enrollment)

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'classroom', 'start_time', 'end_time', 'days_of_week')
    list_filter = ('days_of_week', 'classroom')
    search_fields = ('lesson__name', 'classroom__room_number')

    def days_of_week(self, obj):
        return ', '.join(obj.get_days_of_week_display())

admin.site.register(Timetable)