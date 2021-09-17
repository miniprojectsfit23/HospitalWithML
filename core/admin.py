from django.contrib import admin
from .models import User,Doctor,Patient
from django import forms


class UserDoctorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('activated', 'isDoctor', 'first_name',
                  'last_name', 'username', 'specialization','patients',)


class UserPatientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('activated', 'isDoctor', 'first_name', 'last_name',
                  'username', 'age', 'disease', 'allergies')

class UserAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        if obj.isDoctor:
            return UserDoctorForm
        else:
            return UserPatientForm

class DoctorUserAdmin(UserAdmin):
	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		return qs.filter(isDoctor__exact=True)


class PatientUserAdmin(UserAdmin):
	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		return qs.filter(isDoctor__exact=False)

admin.site.register(Patient, PatientUserAdmin)
admin.site.register(Doctor, DoctorUserAdmin)