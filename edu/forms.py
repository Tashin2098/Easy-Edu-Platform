from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Grades




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
    search_recipient = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search recipient by name'}),
    )

    class Meta:
        model = models.Message
        fields = ['recipient', 'content', 'attachment', 'image']  # Do not include search_recipient here

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MessageForm, self).__init__(*args, **kwargs)
        if is_teacher(user):
            self.fields['recipient'].queryset = User.objects.filter(groups__name='STUDENT')
            self.fields['recipient'].empty_label = "Students"
        else:
            self.fields['recipient'].queryset = User.objects.filter(groups__name='TEACHER')
            self.fields['recipient'].empty_label = "Teachers"
        self.fields['recipient'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['attachment'].required = False
        self.fields['image'].required = False



class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'


class ConsultationHourForm(forms.ModelForm):
    class Meta:
        model = models.ConsultationHour
        fields ='__all__'  # Add 'teacher' field to the form


grade_choices=(('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'))
class GradesForm(forms.Form):
   
   grade_sheet=forms.ChoiceField( choices=grade_choices)

class AskCourseForm(forms.Form):
    course = forms.CharField(max_length=100)







    









