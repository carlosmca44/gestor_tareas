from django.shortcuts import render, redirect
from .models import Tarea
from .forms import *
from django.contrib.auth.decorators import login_required
from .binary_search import binary_seacrh
from .heap_sort import heap_sort


def sign_in(request):
    if request.method == 'POST':
        form = create_user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = create_user_form()

    context = {'form': form}
    return render(request, 'auth/signin.html', context)


@login_required
def home(request):
    tareas_list = list(Tarea.objects.filter(user=request.user))
    context = {'tareas': tareas_list}
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


def binary_search_view(request):
    tareas = Tarea.objects.filter(user=request.user)
    tareas_list = []
    element_to_show = 0
    for tarea in tareas:
        tareas_list.append(tarea.id)

    if request.method == "POST":
        form = binarySearchForm(request.POST)
        if form.is_valid():
            form.save()
            number_to_search = bsElement.objects.all()
            for i in number_to_search:
                element_to_show = binary_seacrh(tareas_list, i.id_number)
                bsElement.objects.filter(id_number=i.id_number).delete()
            if element_to_show != -1:
                tarea = Tarea.objects.filter(id=tareas_list[element_to_show])
    else:
        form = binarySearchForm()

    context = {'form': form, 'tarea': tarea}
    return render(request, 'binary_search/binary_search.html', context)


def heap_sort_view(request):
    tareas_list_ordered = list(Tarea.objects.filter(user=request.user))

    listado = []

    for i in tareas_list_ordered:
        listado.append([i.prioridad, i.id])

    heap_sort(listado)
    listado.sort(reverse=True)

    to_return = []

    for i in listado:
        for j in tareas_list_ordered:
            if i[1] == j.id:
                to_return.append(j)

    context = {'tareas': to_return}
    return render(request, 'home/home.html', context)
