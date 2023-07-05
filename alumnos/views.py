from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    #select * from productos
    #context={}, context
    productos = Producto.objects.all()
    data = {"productos": productos}
    return render(request, 'alumnos/index.html', data)


def agregar_producto(request):
    data = {'form': ProductoForm()}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario

    return render(request, 'alumnos/producto/agregar.html', data)
