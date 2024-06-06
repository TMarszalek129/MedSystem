from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import datetime
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
    patient_birth = int(patient.birthdate.strftime("%Y"))
    today = datetime.datetime.today().year
    age = today - patient_birth
    template = loader.get_template('details.html')
    context = {
        'pt': patient,
        'age' : age
    }
    return HttpResponse(template.render(context, request))

def exams(request, id):
    measurements = models.Measurement.objects.filter(patient_id=id).values()


    # vals[0]['patient_id_id']

    for m in measurements:
        measure = models.Measure.objects.get(id=m['measure_id_id'])
        m['unit'] = measure.unit_id
        m['measure'] = measure.measure_name

    template = loader.get_template('exams.html')
    context = {
        'm' : measurements,
        'id' : id
    }
    return HttpResponse(template.render(context, request))
def new_measurement(request, id):
    if request.method == 'GET':
        form = forms.FormMeasurement()
    else:
        form = forms.FormMeasurement(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.patient_id = models.Patient.objects.get(id=id)
            measurement.save()
            return redirect('/patients/details/' + str(id))

    return render(request, "new_measurement.html", {"f": form, "id": id})



def testing(request):
    mydata = models.Patient.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'patients': mydata,
    }
    return HttpResponse(template.render(context, request))