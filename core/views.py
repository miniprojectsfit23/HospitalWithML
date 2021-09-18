from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from core.forms import RegisterDoctorForm, RegisterPatientForm,LoginFormDoctor,LoginFormPatient
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import User
from django.http import Http404


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

class RegisterDoctorView(SuccessMessageMixin,CreateView):
    form_class = RegisterDoctorForm
    success_url = "/login-doctor/"
    template_name = 'core/signup.html'
    success_message = "You have been registered successfully. Please contact Administrator for activation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Register As Doctor"
        return context


class RegisterPatientView(SuccessMessageMixin,CreateView):
    form_class = RegisterPatientForm
    success_url = "/login-patient/"
    template_name = 'core/signup.html'
    success_message = "You have been registered successfully. Please contact Administrator for activation"

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
        elif not user:
            messages.add_message(request, messages.ERROR, "Invalid Credentials")
            return render(request, 'core/login.html', {'title':'Login as Patient','form': form })
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
        elif not user:
            messages.add_message(request, messages.ERROR, "Invalid Credentials")
            return render(request, 'core/login.html', {'title':'Login as Patient','form': form })
        else:
            if user:
                login(request, user)
                return redirect("/")# Redirect to a success page.
    return render(request, 'core/login.html', {'title':'Login as Patient','form': form })

def logout_core(request):
    logout(request)
    return redirect("/")

def add_remove_patients(request):
    if request.user.is_authenticated:
        if request.user.isDoctor:
            if request.POST:
                if request.POST['toggle']=='add':
                    request.user.patients.add(User.objects.get(username=request.POST['add_patlist']))
                    return redirect("/edit-patients/")
                else:
                    request.user.patients.remove(User.objects.get(username=request.POST['remove_patlist']))
                    return redirect("/edit-patients/")
            else:
                rem_patients=request.user.patients.all()
                add_patients=User.objects.filter(isDoctor=False)
                for patient in rem_patients:
                    add_patients=add_patients.exclude(username=patient.username)
                return render(request, 'core/edit_patients.html', {'title':'Edit Patients', 'rem_patients':rem_patients,'add_patients':add_patients })
        else:
            return redirect("/")
    else:
        return redirect("/")
class UpdatePatientView(SuccessMessageMixin,UpdateView):
    model=User
    form_class = RegisterPatientForm
    success_url = "/login-patient/"
    template_name = 'core/update.html'
    success_message = "Your account has been updated successfully. You need to login again"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Patient"
        return context
    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            raise Http404("You're not logged in")
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj

class UpdateDoctorView(SuccessMessageMixin,UpdateView):
    model=User
    form_class = RegisterDoctorForm
    success_url = "/login-doctor/"
    template_name = 'core/update.html'
    success_message = "Your account has been updated successfully. You need to login again"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Doctor"
        return context
    def get_object(self, queryset=None):
        if not self.request.user.is_authenticated:
            raise Http404("You're not logged in")
        if queryset is None:
            queryset = self.get_queryset()   # This should help to get current user 

        # Next, try looking up by primary key of Usario model.
        queryset = queryset.filter(pk=self.request.user.pk)


        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj