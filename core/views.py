from django.shortcuts import render
from django.views.generic import CreateView
from core.forms import RegisterDoctorForm, RegisterPatientForm,LoginFormDoctor,LoginFormPatient
from django.contrib.auth import login,logout
from django.shortcuts import redirect

# Create your views here.


def homeview(request):
    if request.user.is_authenticated:
        if request.user.activated:
            if request.user.isDoctor:
                return render(request, 'core/doctor_home.html', {'title':'Doctor'})
            else:
                return render(request, 'core/patient_home.html', {'title':'Patient'})
        else:
            return render(request, 'core/not_activated.html', {'title':'Contact Admin'})
    else:
        return render(request, 'core/home.html', {'title':'Home'})

class RegisterDoctorView(CreateView):
    form_class = RegisterDoctorForm
    success_url = "/login-doctor/"
    template_name = 'core/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Register As Doctor"
        return context


class RegisterPatientView(CreateView):
    form_class = RegisterPatientForm
    success_url = "/login-patient/"
    template_name = 'core/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Register As Patient"
        return context

def login_view_doctor(request):
    form = LoginFormDoctor(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user == -1:
            return render(request, 'core/login.html', {'title':'Login as Doctor','form': form })
        else:
            if user:
                login(request, user)
                return redirect("/")# Redirect to a success page.
    return render(request, 'core/login.html', {'title':'Login as Doctor','form': form })

def login_view_patient(request):
    form = LoginFormPatient(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user == -1:
            return render(request, 'core/login.html', {'title':'Login as Patient','form': form })
        else:
            if user:
                login(request, user)
                return redirect("/")# Redirect to a success page.
    return render(request, 'core/login.html', {'title':'Login as Patient','form': form })

def logout_core(request):
    logout(request)
    return redirect("/")