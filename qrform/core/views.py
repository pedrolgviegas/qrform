from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qrform.core.forms import CoreForm
from qrform.core.models import ContactUs, Team


def home(request):

    if request.method == 'POST':
        return create(request)

    else:
        return new(request)

def create(request):

    form = CoreForm(request.POST)
    teams = Team.objects.all()

    if not form.is_valid():
        return render(request, 'core/index.html', {'form': form, 'teams': teams})

    # save Core
    ContactUs.objects.create(**form.cleaned_data)

    # message feedback
    messages.success(request, 'Mensagem Enviada com Sucesso!')

    return HttpResponseRedirect('/')

def new(request):

    teams = Team.objects.all()
    return render(request, 'core/index.html', {'form': CoreForm(), 'teams': teams})
