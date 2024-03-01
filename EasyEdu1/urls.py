"""
URL configuration for EasyEdu1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from edu import views
from django.contrib.auth.views import LoginView,LogoutView

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
    path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
    path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
]
