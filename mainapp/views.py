from email import message
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from mainapp.forms import DepartmentForm, UpdateProfileForm, CustomUserCreationForm, TimeRecordForm
from mainapp.models import EmployeeProfile, TimeRecord, Department, JobRole
import datetime

class IndexView(LoginRequiredMixin, TemplateView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/profile.html'

class UpdateProfileView(LoginRequiredMixin, FormView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/profile_update_form.html'
  form_class = UpdateProfileForm
  success_url = '/profile/'

  def form_valid(self, form):
    e = EmployeeProfile.objects.get(user=self.request.user)
    e.user.first_name = form.cleaned_data['first_name']
    e.user.last_name = form.cleaned_data['last_name']
    e.user.email = form.cleaned_data['email']
    e.user.save()
    e.save()
    f = UpdateProfileForm(self.request.POST, instance=e)
    f.save()
    return super().form_valid(form)
  
  def get_initial(self):
    initial = super().get_initial()
    e = EmployeeProfile.objects.get(user=self.request.user)
    initial['first_name'] = e.user.first_name
    initial['last_name'] = e.user.last_name
    initial['email'] = e.user.email
    initial['address'] = e.address
    initial['phone_no'] = e.phone_no
    return initial

class ManageView(LoginRequiredMixin, TemplateView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/manage.html'

class ViewEmployeesView(LoginRequiredMixin, ListView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/view_employees.html'
  model = User
  context_object_name = 'user_list'

  def get_queryset(self):
    return User.objects.exclude(is_superuser=True).exclude(
      username=self.request.user.username)

class AddEmployeeView(LoginRequiredMixin, FormView):
  login_url = '/login/'
  redirect_field_name = '' 
  template_name = 'mainapp/add_employee_form.html'
  success_url = '/manage/add-employee-success/'
  form_class = CustomUserCreationForm

  def form_valid(self, form):
    u = User.objects.create_user(form.cleaned_data.get('username'),
      password=form.cleaned_data.get('password1'))
    u.first_name = form.cleaned_data.get('first_name')
    u.last_name = form.cleaned_data.get('username')
    u.email = form.cleaned_data.get('email')
    u.save()
    # u.refresh_from_db()
    # # Additional fields for Employee
    # u.employeeprofile.address = form.cleaned_data.get('address')
    # u.employeeprofile.save()
    # u.save()
    return super().form_valid(form)

class AddEmployeeSuccessView(LoginRequiredMixin, View):
  login_url = '/login/'
  redirect_field_name = ''

  def get(self, request, *args, **kwargs):
      return render(request, 'mainapp/add_employee_success.html', {'message': 'Employee added'})

class DeleteEmployeesView(LoginRequiredMixin, ListView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/delete_employees.html'
  model = User
  context_object_name = 'user_list'

  def get_queryset(self):
    return User.objects.exclude(is_superuser=True).exclude(
      username=self.request.user.username)

  def post(self, request, *args, **kwargs):
    username_list = request.POST.getlist('username')
    
    for username in username_list:
      u = User.objects.get(username=username)
      u.delete()
    return redirect('mainapp:delete-employees')

class UpdateEmployeeSelectView(LoginRequiredMixin, ListView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/update_employee_select.html'
  model = User
  context_object_name = 'user_list'

  def get_queryset(self):
    return User.objects.exclude(is_superuser=True).exclude(
      username=self.request.user.username)
  
  def post(self, request, *args, **kwargs):
    selected_username = request.POST.get('username')
    u = get_object_or_404(User, username=selected_username)
    return redirect("mainapp:update-employee-form", pk=u.pk)

class UpdateEmployeeFormView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'mainapp/update_employee_form.html'
    fields = ['first_name', 'last_name', 'email' ]
    success_url = "/manage/update-employee/"

class TimeView(LoginRequiredMixin, View):
  login_url = '/login/'
  redirect_field_name = ''
  form_class = TimeRecordForm
  template_name = 'mainapp/time.html'

  def get(self, request, *args, **kwargs):
    initial = None
    date_query = None

    try:
      date_query = self.kwargs['date']
      initial = {'date': date_query}
    except:
      today = datetime.date.today()
      date_query = today.today()
      initial = {'date': date_query}

    form = self.form_class(initial=initial)
    time_records = TimeRecord.objects.filter(date=date_query, user=request.user)

    # Compute total hours
    tot_work_hrs = datetime.timedelta()
    for tr in time_records:
      if tr.action.lower() == 'work':
        tot_work_hrs += datetime.datetime.combine(datetime.date.today(), tr.time_out) - datetime.datetime.combine(datetime.date.today(), tr.time_in)

    return render(request, self.template_name, {'form': form, 'time_records': time_records, 'tot_work_hrs': tot_work_hrs})

  def post(self, request, *args, **kwargs):
    tr_obj = TimeRecord(user=request.user)
    form = self.form_class(request.POST, instance=tr_obj)

    if form.is_valid():
      form.save()      
      try:
        return HttpResponseRedirect(f"/time/{self.kwargs['date']}")
      except:
        return HttpResponseRedirect(f"/time/")
    return render(request, self.template_name, {'form': form})

class DeleteTimeRecordRedirectView(LoginRequiredMixin, RedirectView):
  login_url = '/login/'
  redirect_field_name = ''  
  permanent = False
  query_string = False
  pattern_name = 'mainapp:time'

  def get_redirect_url(self, *args, **kwargs):
    tr_obj = get_object_or_404(TimeRecord, pk=kwargs['pk'])
    tr_obj.delete()

    return super().get_redirect_url(date=kwargs['date'])

class DepartmentView(LoginRequiredMixin, TemplateView):
  login_url = '/login/'
  redirect_field_name = ''
  template_name = 'mainapp/departments.html'
  form_class = DepartmentForm

  def get(self, request, *args, **kwargs):
    # Get request, return and display department list
    context = {}
    form = self.form_class()
    context['form'] = form
    d = Department.objects.all()
    context['department_list'] = d

    if kwargs:
      context['messages'] = kwargs['messages']
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)

    if form.is_valid():
      messages = ''
      action = request.POST['action']

      if action.lower() == 'delete':
        # Delete selected departments
        is_deleted = False
        for name in request.POST.getlist('select_departments'):
          if name != None:
            try:
              d = Department.objects.get(name=name)
              d.delete()
              messages += f"{name} "
              is_deleted = True
            except:
              messages = f"{name} not found"
        if not is_deleted:
          messages = 'No record deleted'
        else:
          messages += 'deleted'
      elif action.lower() == 'add':
        # Add new deparment object
        if form.cleaned_data['name']:
          messages = f"{form.cleaned_data['name']} added"
          form.save()
        else:
          messages = 'No record added'

      if messages:
        return redirect('mainapp:departments', messages=messages)
      else:
        return redirect('mainapp:departments')

    # TODO improve, incase form submitted is invalid
    d = Department.objects.all()
    return render(request, self.template_name, {'form': form, 'department_list': d })

class TmpView(TemplateView):
  template_name = 'mainapp/tmp.html'
