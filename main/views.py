from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'home/home.html', context)

def add(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form': form}
    return render(request, 'home/add.html', context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id = tarea_id)
    tarea.delete()
    return redirect(home)
def ordenar():
    objeto=Tarea.get(id=tarea_id)
def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
            form = TareaForm(instance=tarea)
    context = {'form': form }
    return render (request, 'home/editar.html', context)        
            

def personal(request):
    return render(request, 'personal/personal.html')

def trabajos(request):
    return render(request, 'trabajos/trabajo.html')

def lista(request):
    return render(request, 'listas/lista.html') 

def birthday(request):
    return render(request, 'birthday/birthday.html')
    
    
# Create your views here.
