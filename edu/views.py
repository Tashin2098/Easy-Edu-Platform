from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
def homepage(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request, "index.html")
def aboutUs(request):
    return render(request,"aboutus.html")
def adminView(request):
    return render(request,'adminView.html')

def studentDash(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'studentdashboard.html')
def teacherView(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'teacherview.html')
def admin_signup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request, 'admin_signup.html',{'form':form})

def student_signup(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtra_info_form()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtra_info_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            f2.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    


    return render(request, "student_signup.html",context=mydict)

def teacher_signup(request):
    form1=forms.TeacherUserForm()
    form2=forms.TeacherExtra_info_form()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.TeacherUserForm(request.POST)
        form2=forms.TeacherExtra_info_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            f2.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('teacherlogin')
    


    return render(request, "teacher_signup.html",context=mydict)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()
def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def afterlogin(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_student(request.user):
         accountapproval=models.StudentExtra_info.objects.all().filter(user_id=request.user.id,status=True)
         if accountapproval:
             return redirect('student-dashboard')
         else:
             return render(request,'std_wait_forapprove.html')
         
    elif is_teacher(request.user):
         accountapproval=models.TeacherExtra_info.objects.all().filter(user_id=request.user.id,status=True)
         if accountapproval:
             return redirect('teacher-dashboard')
         else:
             return render(request,'teacher_wait_forapprove.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    teachercount=models.TeacherExtra_info.objects.all().filter(status=True).count()
    pendingteachercount=models.TeacherExtra_info.objects.all().filter(status=False).count()

    studentcount=models.StudentExtra_info.objects.all().filter(status=True).count()
    pendingstudentcount=models.StudentExtra_info.objects.all().filter(status=False).count()

    teachersalary=models.TeacherExtra_info.objects.filter(status=True).aggregate(Sum('salary'))
    pendingteachersalary=models.TeacherExtra_info.objects.filter(status=False).aggregate(Sum('salary'))

    studentfee=models.StudentExtra_info.objects.filter(status=True).aggregate(Sum('fee',default=0))
    pendingstudentfee=models.StudentExtra_info.objects.filter(status=False).aggregate(Sum('fee'))

    # notice=models.Notice.objects.all()
    mydict={
        'teachercount':teachercount,
        'pendingteachercount':pendingteachercount,

        'studentcount':studentcount,
        'pendingstudentcount':pendingstudentcount,

        'teachersalary':teachersalary['salary__sum'],
        'pendingteachersalary':pendingteachersalary['salary__sum'],

        'studentfee':studentfee['fee__sum'],
        'pendingstudentfee':pendingstudentfee['fee__sum'],

        # 'notice':notice

    }

    return render(request,'admin_dashboard.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_teacherview(request):
    return render(request,'admin_teacher.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_teacher_view(request):
    teachers=models.TeacherExtra_info.objects.all().filter(status=True)
    return render(request,'admin_view_teacher.html',{'teachers':teachers})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_teacher_view(request):
    teachers=models.TeacherExtra_info.objects.all().filter(status=False)
    return render(request,'admin_approve_teacher.html',{'teachers':teachers})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_teacher_view(request,pk):
    teacher=models.TeacherExtra_info.objects.get(id=pk)
    teacher.status=True
    teacher.save()
    return redirect(reverse('admin-approve-teacher'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_teacher_view(request,pk):
    teacher=models.TeacherExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return redirect('admin-approve-teacher')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_teacher_salary_view(request):
    teachers=models.TeacherExtra_info.objects.all().filter(status=True)
    return render(request,'admin_view_teacher_salary.html',{'teachers':teachers})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_studentview(request):
    return render(request,'admin_student.html')

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    return render(request,'student_dashboard.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    return render(request,'teacher_dashboard.html')