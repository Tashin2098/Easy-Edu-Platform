from django import forms
from django.contrib.auth.models import User
from . import models




class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtra_info_form(forms.ModelForm):
    class Meta:
        model=models.StudentExtra_info
        fields=['roll','cl','mobile','fee','status']

class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class TeacherExtra_info_form(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra_info
        fields=['salary','mobile','status']



class class1to3SigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class class4to8SigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class class9to10SigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class class11to12SigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class financeSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']    

class webdesignSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']  

presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()

def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['recipient', 'content', 'attachment']  # Include recipient field

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Get the user passed from the view
        super(MessageForm, self).__init__(*args, **kwargs)
        # Filter recipients based on user type (teacher can only message students)
        if is_teacher(user):
            students = User.objects.filter(groups__name='STUDENT')
            self.fields['recipient'].queryset = students
            self.fields['recipient'].empty_label = "Students"
        else:  # Assuming a student can only message teachers
            teachers = User.objects.filter(groups__name='TEACHER')
            self.fields['recipient'].queryset = teachers
            self.fields['recipient'].empty_label = "Teachers"
        # Customize label to display first name and last name
        self.fields['recipient'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['attachment'].required = False

class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'


class ConsultationHourForm(forms.ModelForm):
    class Meta:
        model = models.ConsultationHour
        fields ='__all__'  # Add 'teacher' field to the form








