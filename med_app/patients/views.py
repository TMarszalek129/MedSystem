from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from . import models, forms

def main(request):

    if request.method == 'GET':
        form = forms.FormLogin()
    else:
        form = forms.FormLogin(request.POST)


        if form.is_valid():
            login_data = request.POST['login']
            pwd_data = request.POST['password']

            try:
                patient = models.Patient.objects.get(login=login_data, password=pwd_data)
            except models.Patient.DoesNotExist:
                patient = None


            if patient is not None:
                return redirect('patients/details/' + str(patient.id))

    return render(request, 'main.html', {'f': form})

def signup(request):
    if request.method == 'GET':
        form = forms.FormPatient()
    else:
        form = forms.FormPatient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    return render(request, "registration/signup.html", {"f":form})

def change_pass(request):
    if request.method == 'GET':
        form = forms.FormChangePassword()
    else:
        form = forms.FormChangePassword(request.POST)
        if form.is_valid():
            login_data = request.POST['login']
            pwd_old = request.POST['oldpassword']
            pwd_new = request.POST['newpassword']

            try:
                patient = models.Patient.objects.get(login=login_data, password=pwd_old)
                patient.password = pwd_new
                patient.save(update_fields=['password'])
            except models.Patient.DoesNotExist:
                patient = None
                print('Patient does not exists')
            if patient is not None:
                return redirect('main')

    return render(request, "registration/change_pass.html", {"f":form})


def patients(request):
    allpatients = models.Patient.objects.all().values()
    template = loader.get_template('all_patients.html')
    context = {
        'patients': allpatients,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    patient = models.Patient.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'pt': patient,
    }
    return HttpResponse(template.render(context, request))



def testing(request):
    mydata = models.Patient.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'patients': mydata,
    }
    return HttpResponse(template.render(context, request))