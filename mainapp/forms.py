from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm, DateInput, TimeInput
from django.contrib.auth.models import User
from mainapp.models import Department, EmployeeProfile, TimeRecord
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class CustomUserCreationForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, required=False)
  last_name = forms.CharField(max_length=30, required=False)
  email = forms.EmailField(max_length=30, required=False)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

class UpdateProfileForm(ModelForm):
  first_name = forms.CharField(max_length=30, required=False)
  last_name = forms.CharField(max_length=30, required=False)
  email = forms.EmailField(max_length=30, required=False)

  class Meta:
    model = EmployeeProfile
    fields = ['first_name', 'last_name', 'email', 'address', 'phone_no']

class TimeRecordForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['date'].initial = datetime.now().date()
    self.fields['time_in'].initial = datetime.now().replace(second=0, microsecond=0)
    self.fields['time_out'].initial = datetime.now().replace(second=0, microsecond=0)
      
  class Meta:
    model = TimeRecord
    exclude = ['user',]

    widgets = {
      'date': DateInput(attrs={'type': 'date', 'oninput': 'goToDateFunc()'}),
      'time_in': TimeInput(attrs={'type': 'time'}),
      'time_out': TimeInput(attrs={'type': 'time'}),
    }

class DepartmentForm(ModelForm):
  class Meta:
    model = Department
    fields = '__all__'