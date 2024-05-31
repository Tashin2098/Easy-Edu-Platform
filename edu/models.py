from django.db import models
from django.contrib.auth.models import User

# Create your models here.
classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]

class StudentExtra_info(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=12,choices=classes,default='one')
    #cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class TeacherExtra_info(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40,null=True)
    #cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    
class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=12)
    present_status = models.CharField(max_length=10)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    attachment = models.FileField(upload_to='message_attachments/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True) 
    def __str__(self):
        return f"From {self.sender.first_name} to {self.recipient.first_name} at {self.timestamp}"
    

class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='education')
    
    message=models.CharField(max_length=500)


class ConsultationHour(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    class_link = models.URLField()
    given_by=models.CharField(max_length=20,null=True,default='education')


    def __str__(self):
        return f"{self.day} - {self.time}"

class Grades(models.Model):
    roll=models.CharField(max_length=10,null=True)
    cl=models.CharField(max_length=12)
    grade_sheet = models.CharField(max_length=2, choices=[('A+', 'A+'), ('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')])





