from django.urls import path
from . import views

app_name="core"
urlpatterns = [
	path("",views.homeview,name="home"),
	path("register-doctor/",views.RegisterDoctorView.as_view(),name="register-doctor"),
	path("register-patient/",views.RegisterPatientView.as_view(),name="register-patient"),
	path("login-doctor/",views.login_view_doctor,name="login-doctor"),
	path("login-patient/",views.login_view_patient,name="login-patient"),
	path("logout/",views.logout_core,name="logout"),
]