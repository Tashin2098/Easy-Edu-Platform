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
def blogs(request):
    return render(request,"blogs.html")

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
         


    elif is_class1to3(request.user):
        return redirect('class1to3video')
    elif is_class4to8(request.user):
        return redirect('class4to8video')
    elif is_class9to10(request.user):
        return redirect('class9to10video')
    elif is_class11to12(request.user):
        return redirect('class11to12video')
    elif is_finance(request.user):
        return redirect('financevideo')
    elif is_webdesign(request.user):
        return redirect('webdesignvideo')


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
def admin_add_teacher_view(request):
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
            f2.status=True
            f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-teacher')
    return render(request,'admin_add_teacher.html',context=mydict)

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
def delete_teacher_from_school_view(request,pk):
    teacher=models.TeacherExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return redirect('admin-view-teacher')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_teacher_view(request,pk):
    teacher=models.TeacherExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=teacher.user_id)

    form1=forms.TeacherUserForm(instance=user)
    form2=forms.TeacherExtra_info_form(instance=teacher)
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        form1=forms.TeacherUserForm(request.POST,instance=user)
        form2=forms.TeacherExtra_info_form(request.POST,instance=teacher)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-teacher')
    return render(request,'admin_update_teacher.html',context=mydict)

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


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_dashboard_view(request):
    teacherdata=models.TeacherExtra_info.objects.all().filter(status=True,user_id=request.user.id)
    #notice=models.Notice.objects.all()
    mydict={
        'salary':teacherdata[0].salary,
        'mobile':teacherdata[0].mobile,
        'date':teacherdata[0].joindate,
        # 'notice':notice
    }
    return render(request,'teacher_dashboard.html',context=mydict)

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_attendance_view(request):
    return render(request,'teacher_attendance.html')

@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_take_attendance_view(request,cl):
    students=models.StudentExtra_info.objects.all().filter(cl=cl)
    aform=forms.AttendanceForm()
    if request.method=='POST':
        form=forms.AttendanceForm(request.POST)
        if form.is_valid():
            Attendances=request.POST.getlist('present_status')
            date=form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel=models.Attendance()
                AttendanceModel.cl=cl
                AttendanceModel.date=date
                AttendanceModel.present_status=Attendances[i]
                AttendanceModel.roll=students[i].roll
                AttendanceModel.save()
            return redirect('teacher-attendance')
        else:
            print('form invalid')
    return render(request,'teacher_take_attendance.html',{'students':students,'aform':aform})


@login_required(login_url='teacherlogin')
@user_passes_test(is_teacher)
def teacher_view_attendance_view(request,cl):
    form=forms.AskDateForm()
    if request.method=='POST':
        form=forms.AskDateForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data['date']
            attendancedata=models.Attendance.objects.all().filter(date=date,cl=cl)
            studentdata=models.StudentExtra_info.objects.all().filter(cl=cl)
            mylist=zip(attendancedata,studentdata)
            return render(request,'teacher_view_attendance_page.html',{'cl':cl,'mylist':mylist,'date':date})
        else:
            print('form invalid')
    return render(request,'teacher_view_attendance_ask_date.html',{'cl':cl,'form':form})



@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    studentdata=models.StudentExtra_info.objects.all().filter(status=True,user_id=request.user.id)
    #notice=models.Notice.objects.all()
    mydict={
        'roll':studentdata[0].roll,
        'mobile':studentdata[0].mobile,
        'fee':studentdata[0].fee,
        # 'notice':notice
    }
    return render(request,'student_dashboard.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_student_view(request):
    students=models.StudentExtra_info.objects.all().filter(status=True)
    return render(request,'admin_view_student.html',{'students':students})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_student_view(request):
    students=models.StudentExtra_info.objects.all().filter(status=False)
    return render(request,'admin_approve_student.html',{'students':students})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_student_view(request,pk):
    students=models.StudentExtra_info.objects.get(id=pk)
    students.status=True
    students.save()
    return redirect(reverse('admin-approve-student'))

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_student_view(request,pk):
    student=models.StudentExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return redirect('admin-approve-student')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_student_view(request,pk):
    student=models.StudentExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=student.user_id)
    form1=forms.StudentUserForm(instance=user)
    form2=forms.StudentExtra_info_form(instance=student)
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST,instance=user)
        form2=forms.StudentExtra_info_form(request.POST,instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.status=True
            f2.save()
            return redirect('admin-view-student')
    return render(request,'admin_update_student.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_student_view(request,pk):
    student=models.StudentExtra_info.objects.get(id=pk)
    user=models.User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return redirect('admin-approve-student')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_student_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtra_info_form()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtra_info_form(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-student')
    return render(request,'admin_add_student.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_student_fee_view(request):
    students=models.StudentExtra_info.objects.all().filter(status=True)
    return render(request,'admin_fee_view_student.html',{'students':students})



def class1to3View(request):
    return render(request,'class1to3View.html')


def class1to3_signup_view(request):
    form=forms.class1to3SigupForm()
    if request.method=='POST':
        form=forms.class1to3SigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_class1to3_group = Group.objects.get_or_create(name='class1to3')
            my_class1to3_group[0].user_set.add(user)

            return HttpResponseRedirect('class1to3login')
    return render(request, 'class1to3signup.html',{'form':form})


def is_class1to3(user):
    return user.groups.filter(name='class1to3').exists()


    
    

@login_required(login_url='class1to3login')
@user_passes_test(is_class1to3)
def class1to3video(request):
   

    return render(request,'class1to3video.html')



def class4to8View(request):
    return render(request,'class4to8View.html')

def class4to8_signup_view(request):
    form=forms.class4to8SigupForm()
    if request.method=='POST':
        form=forms.class4to8SigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_class4to8_group = Group.objects.get_or_create(name='class4to8')
            my_class4to8_group[0].user_set.add(user)

            return HttpResponseRedirect('class4to8login')
    return render(request, 'class4to8signup.html',{'form':form})


def is_class4to8(user):
    return user.groups.filter(name='class4to8').exists()

    

@login_required(login_url='class4to8login')
@user_passes_test(is_class4to8)
def class4to8video(request):
   

    return render(request,'class4to8video.html')


def class9to10View(request):
    return render(request,'class9to10View.html')

def class9to10_signup_view(request):
    form=forms.class9to10SigupForm()
    if request.method=='POST':
        form=forms.class9to10SigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_class9to10_group = Group.objects.get_or_create(name='class9to10')
            my_class9to10_group[0].user_set.add(user)

            return HttpResponseRedirect('class9to10login')
    return render(request, 'class9to10signup.html',{'form':form})


def is_class9to10(user):
    return user.groups.filter(name='class9to10').exists()

    

@login_required(login_url='class9to10login')
@user_passes_test(is_class9to10)
def class9to10video(request):
   

    return render(request,'class9to10video.html')




def class11to12View(request):
    return render(request,'class11to12View.html')

def class11to12_signup_view(request):
    form=forms.class11to12SigupForm()
    if request.method=='POST':
        form=forms.class11to12SigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_class11to12_group = Group.objects.get_or_create(name='class11to12')
            my_class11to12_group[0].user_set.add(user)

            return HttpResponseRedirect('class11to12login')
    return render(request, 'class11to12signup.html',{'form':form})


def is_class11to12(user):
    return user.groups.filter(name='class11to12').exists()


    

@login_required(login_url='class11to12login')
@user_passes_test(is_class11to12)
def class11to12video(request):
   

    return render(request,'class11to12video.html')









def financeView(request):
    return render(request,'financeView.html')

def finance_signup_view(request):
    form=forms.financeSigupForm()
    if request.method=='POST':
        form=forms.financeSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_finance_group = Group.objects.get_or_create(name='finance')
            my_finance_group[0].user_set.add(user)

            return HttpResponseRedirect('financelogin')
    return render(request, 'financesignup.html',{'form':form})


def is_finance(user):
    return user.groups.filter(name='finance').exists()


    

@login_required(login_url='financelogin')
@user_passes_test(is_finance)
def financevideo(request):
   

    return render(request,'financevideo.html')








def webdesignView(request):
    return render(request,'webdesignView.html')

def webdesign_signup_view(request):
    form=forms.webdesignSigupForm()
    if request.method=='POST':
        form=forms.webdesignSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_webdesign_group = Group.objects.get_or_create(name='webdesign')
            my_webdesign_group[0].user_set.add(user)

            return HttpResponseRedirect('webdesignlogin')
    return render(request, 'webdesignsignup.html',{'form':form})


def is_webdesign(user):
    return user.groups.filter(name='webdesign').exists()


    

@login_required(login_url='webdesignlogin')
@user_passes_test(is_webdesign)
def webdesignvideo(request):
   

    return render(request,'webdesignvideo.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_attendance_view(request):
    return render(request,'admin_attendance.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_take_attendance_view(request,cl):
    students=models.StudentExtra_info.objects.all().filter(cl=cl)
    print(students)
    aform=forms.AttendanceForm()
    if request.method=='POST':
        form=forms.AttendanceForm(request.POST)
        if form.is_valid():
            Attendances=request.POST.getlist('present_status')
            date=form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel=models.Attendance()
                AttendanceModel.cl=cl
                AttendanceModel.date=date
                AttendanceModel.present_status=Attendances[i]
                AttendanceModel.roll=students[i].roll
                AttendanceModel.save()
            return redirect('admin-attendance')
        else:
            print('form invalid')
    return render(request,'admin_take_attendance.html',{'students':students,'aform':aform})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_attendance_view(request,cl):
    form=forms.AskDateForm()
    if request.method=='POST':
        form=forms.AskDateForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data['date']
            attendancedata=models.Attendance.objects.all().filter(date=date,cl=cl)
            studentdata=models.StudentExtra_info.objects.all().filter(cl=cl)
            mylist=zip(attendancedata,studentdata)
            return render(request,'admin_view_attendance_page.html',{'cl':cl,'mylist':mylist,'date':date})
        else:
            print('form invalid')
    return render(request,'admin_view_attendance_ask_date.html',{'cl':cl,'form':form})

