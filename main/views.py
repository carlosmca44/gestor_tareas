from django.shortcuts import render, redirect
from .models import Tarea
from .forms import *
from django.contrib.auth.decorators import login_required
from .binary_search import binary_seacrh


def signIn(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = createUserForm()

    context = {'form': form}
    return render(request, 'auth/signin.html', context)


@login_required
def home(request):
    tareas = Tarea.objects.filter(user=request.user)
    context = {'tareas': tareas}
    return render(request, 'home/home.html', context)


@login_required
def add(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user
            tarea.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form': form}
    return render(request, 'home/add.html', context)


@login_required
def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect(home)


def ordenar():
    objeto = Tarea.get(id=tarea_id)


@login_required
def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form}
    return render(request, 'home/editar.html', context)


def personal(request):
    return render(request, 'personal/personal.html')


def trabajos(request):
    return render(request, 'trabajos/trabajo.html')


def lista(request):
    return render(request, 'listas/lista.html')


def birthday(request):
    return render(request, 'birthday/birthday.html')


def binary_searchView(request):
    tareas = Tarea.objects.filter(user=request.user)
    tareas_list = []
    elementToShow = 0
    for tarea in tareas:
        tareas_list.append(tarea.id)

    if request.method == "POST":
        form = binarySearchForm(request.POST)
        if form.is_valid():
            form.save()
            numberToSearch = bsElement.objects.all()
            for i in numberToSearch:
                elementToShow = binary_seacrh(tareas_list, i.id_number)
                bsElement.objects.filter(id_number=i.id_number).delete()
            if elementToShow != -1:
                tarea = Tarea.objects.filter(id=tareas_list[elementToShow])
    else:
        form = binarySearchForm()

    context = {'form': form, 'tarea': tarea}
    return render(request, 'binary_search/binary_search.html', context)
