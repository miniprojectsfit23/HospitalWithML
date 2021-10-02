from django.urls import path
from . import views

app_name="ml_tools"
urlpatterns = [
	path("",views.list_all,name="list_all"),
	path("heartdisease/",views.heartdisease,name="heartdisease"),
]