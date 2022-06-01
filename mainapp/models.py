from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Department(models.Model):
  name = models.CharField(max_length=30, blank=True, unique=True)
  def __str__(self):
    return self.name

class JobRole(models.Model):
  title = models.CharField(max_length=30, unique=True)
  def __str__(self):
    return self.title

class EmployeeProfile(models.Model):
  GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
  )
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
  job_role = models.ForeignKey(JobRole, on_delete=models.SET_NULL, blank=True, null=True)
  address = models.CharField(max_length=500, blank=True, null=True)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
  phone_no = models.CharField(max_length=20, blank=True, null=True)
  birth_date = models.DateField(blank=True, null=True)
  start_date = models.DateField(blank=True, null=True)
  end_date = models.DateField(blank=True, null=True)
  manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='emp_manager')

  def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
  if created:
    EmployeeProfile.objects.create(user=instance)
    instance.employeeprofile.save()

class TimeRecord(models.Model):
  ACTION_CHOICES = (
    ('work', 'Work'),
    ('break', 'Break'),
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField()
  time_in = models.TimeField()
  time_out = models.TimeField()
  action = models.CharField(max_length=5, choices=ACTION_CHOICES)
  comments = models.TextField(null=True, blank=True)

  def __str__(self):
    return f"{self.user.username} {self.date} {self.action}"
