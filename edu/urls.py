from django.contrib import admin
from django.urls import path
from edu import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.homepage),
    path('about-us', views.aboutUs),
    path('admin-page',views.adminView),
    path('admin-signup',views.admin_signup_view),
    path('student-page',views.studentDash),
    path("student-signup",views.student_signup),
    path("teacher-signup",views.teacher_signup),
    path('teacher-page',views.teacherView),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='teacherlogin.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-teacher', views.admin_teacherview,name='admin-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
    path('admin-view-teacher-salary', views.admin_view_teacher_salary_view,name='admin-view-teacher-salary'),
    path('admin-student', views.admin_studentview,name='admin-student'),
    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    # path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('admin-view-student-fee', views.admin_view_student_fee_view,name='admin-view-student-fee'),
    path('blogs', views.blogs),

    path('class1to3page',views.class1to3View),
    path('class1to3-signup',views.class1to3_signup_view),
    path('class1to3login', LoginView.as_view(template_name='class1to3login.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('class1to3video', views.class1to3video,name='class1to3video'),
    path('class4to8page',views.class4to8View),
    path('class4to8-signup',views.class4to8_signup_view),
    path('class4to8login', LoginView.as_view(template_name='class4to8login.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('class4to8video', views.class4to8video,name='class4to8video'),
    path('class9to10page',views.class9to10View),
    path('class9to10-signup',views.class9to10_signup_view),
    path('class9to10login', LoginView.as_view(template_name='class9to10login.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('class9to10video', views.class9to10video,name='class9to10video'),
    path('class11to12page',views.class11to12View),
    path('class11to12-signup',views.class11to12_signup_view),
    path('class11to12login', LoginView.as_view(template_name='class11to12login.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('class11to12video', views.class11to12video,name='class11to12video'),

    path('financepage',views.financeView),
    path('finance-signup',views.finance_signup_view),
    path('financelogin', LoginView.as_view(template_name='financelogin.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('financevideo', views.financevideo,name='financevideo'),

    path('webdesignpage',views.webdesignView),
    path('webdesign-signup',views.webdesign_signup_view),
    path('webdesignlogin', LoginView.as_view(template_name='webdesignlogin.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('webdesignvideo', views.webdesignvideo,name='webdesignvideo'),
    
    
    

    path('admin-attendance', views.admin_attendance_view,name='admin-attendance'),
    path('admin-take-attendance/<str:cl>', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance/<str:cl>', views.admin_view_attendance_view,name='admin-view-attendance'),

    # path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),

    path('teacher-attendance', views.teacher_attendance_view,name='teacher-attendance'),
    path('teacher-take-attendance/<str:cl>', views.teacher_take_attendance_view,name='teacher-take-attendance'),
    path('teacher-view-attendance/<str:cl>', views.teacher_view_attendance_view,name='teacher-view-attendance'),
    
    path('student-attendance', views.student_attendance_view,name='student-attendance'),
    path('financecertificate', views.finance_certificate),
    path('financenextpage', views.finance_nextpage),
    path('financeanotherpage', views.finance_another),
    path('webdesigncertificate', views.webdesign_certificate),
    path('webdesignnextpage', views.webdesign_nextpage),
    path('webdesignanotherpage', views.webdesign_anotherpage),



    path('send-message', views.send_message, name='send_message'),
    path('inbox', views.inbox, name='inbox'),
    path('search-recipient/', views.search_recipient, name='search_recipient'),
    path('sent-messages', views.sent_messages, name='sent_messages'),
    path('message-detail/<int:message_id>/', views.message_detail, name='message_detail'),
    path('admin-notice', views.admin_notice_view,name='admin-notice'),
    path('teacher-notice', views.teacher_notice_view,name='teacher-notice'),
    path('upload_consultation_hour', views.upload_consultation_hour, name='upload_consultation_hour'),
    path('view_consultation_hour', views.view_consultation_hours, name='view_consultation_hour'),

    path('teacher-gradesheet', views.teacher_gradesheet_view,name='teacher-gradesheet'),

    path('teacher-take-gradesheet/<str:cl>', views.teacher_take_gradesheet_view,name='teacher-take-gradesheet'),
    path('teacher-view-gradesheet/<str:cl>', views.teacher_view_gradesheet_view,name='teacher-view-gradesheet'),

    path('student-grade', views.student_gradesheet_view,name='student-grade'),

   
]