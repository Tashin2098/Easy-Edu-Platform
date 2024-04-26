from django.contrib import admin
from .models import Attendance,StudentExtra_info,TeacherExtra_info,Notice
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra_info, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra_info, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

