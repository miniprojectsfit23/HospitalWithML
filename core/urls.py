from django.urls import path
from . import views

app_name="core"
urlpatterns = [
	path("",views.homeview,name="home"),
	path("update_profile_pic/",views.update_profile_pic,name="update_profile_pic"),
	path("register-doctor/",views.RegisterDoctorView.as_view(),name="register-doctor"),
	path("register-patient/",views.RegisterPatientView.as_view(),name="register-patient"),
	path("login-doctor/",views.login_view_doctor,name="login-doctor"),
	path("login-patient/",views.login_view_patient,name="login-patient"),
	path("edit-patients/",views.add_remove_patients,name="edit-paitents"),
	path("delete/",views.delete_view,name="delete"),
	path("update-patient/<uuid:pk>/",views.UpdatePatientView.as_view(),name="update-patient"),
	path("update-doctor/<uuid:pk>/",views.UpdateDoctorView.as_view(),name="update-doctor"),
	path("logout/",views.logout_core,name="logout"),
]