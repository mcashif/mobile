from django.http import HttpResponse
from django.views.generic import FormView
from directme.forms import ClientForm, WorkForm, DriverForm
from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.shortcuts import redirect


def manage_clients(request):

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.address = request.POST.get("add")
            client.clientlattude = request.POST.get("elat")
            client.clientlogitute = request.POST.get("elng")
            client.save()
            return redirect('manage_clients')
    else:
        form = ClientForm()
        return render(request, 'directme/cliententry.html', {'form': form})


def manage_work(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.save()
            return redirect('manage_work')
    else:
        form = WorkForm()
        return render(request, 'directme/managework.html', {'form': form})


def manage_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.save()
            return redirect('manage_driver')
    else:
        form = DriverForm()
        return render(request, 'directme/driverentry.html', {'form': form})
