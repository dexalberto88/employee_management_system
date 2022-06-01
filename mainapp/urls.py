from django.urls import path
from django.contrib.auth import views as auth_views
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('login/', auth_views.LoginView.as_view(
    template_name='mainapp/login.html', next_page='/'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='/login/',
    redirect_field_name='mainapp/login'), name='logout'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('profile/update/', views.UpdateProfileView.as_view(), name='profile-update'),
  path('manage/', views.ManageView.as_view(), name='manage'),
  path('manage/view-employees/', views.ViewEmployeesView.as_view(), name='view-employees'),
  path('manage/add-employee-form/', views.AddEmployeeView.as_view(), name='add-employee-form'),
  path('manage/update-employee/', views.UpdateEmployeeSelectView.as_view(), name='update-employee'),
  path('manage/update-employee-form/<int:pk>/', views.UpdateEmployeeFormView.as_view(), name='update-employee-form'),
  path('manage/delete-employees/', views.DeleteEmployeesView.as_view(), name='delete-employees'),
  path('manage/add-employee-success/', views.AddEmployeeSuccessView.as_view(), name='add-employee-success'),
  path('manage/departments/', views.DepartmentView.as_view(), name='departments'),
  path('manage/departments/<messages>/', views.DepartmentView.as_view(), name='departments'),  
  path('time/', views.TimeView.as_view(), name='time'),
  path('time/<slug:date>/', views.TimeView.as_view(), name='time'),
  path('time/delete/<slug:date>/<int:pk>', views.DeleteTimeRecordRedirectView.as_view(), name='time-delete'),
  path('tmp/', views.TmpView.as_view(), name='tmp'),
]