from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reporte
from .forms import ReporteForm, CambiarEstadoForm

@login_required
def reporte_list(request):
    reportes = Reporte.objects.all().order_by('-fecha_reporte')
    es_entidad = request.user.groups.filter(name='Entidad').exists()
    context = {
        'reportes': reportes,
        'es_entidad': es_entidad
    }
    return render(request, 'reportes/reporte_list.html', context)

@login_required
def reporte_create(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            
            # --- ASIGNAR LATITUD Y LONGITUD DESDE EL MAPA ---
            try:
                lat = request.POST.get('latitud')
                lng = request.POST.get('longitud')
                if lat:
                    reporte.latitud = float(lat)
                if lng:
                    reporte.longitud = float(lng)
            except ValueError:
                # Si algo falla, dejamos los valores como None
                reporte.latitud = None
                reporte.longitud = None
            # ---------------------------------------------------
            
            reporte.ciudadano = request.user
            reporte.save()
            return redirect('reporte_list')
    else:
        form = ReporteForm()
    return render(request, 'reportes/reporte_create.html', {'form': form})

@login_required
def reporte_detail(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    es_entidad = request.user.groups.filter(name='Entidad').exists()
    return render(request, 'reportes/reporte_detail.html', {'reporte': reporte, 'es_entidad': es_entidad})

@login_required
def cambiar_estado(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    if not request.user.groups.filter(name='Entidad').exists():
        return redirect('reporte_list')  # solo entidades pueden cambiar estado

    if request.method == 'POST':
        form = CambiarEstadoForm(request.POST, instance=reporte)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.entidad_responsable = request.user
            reporte.save()
            return redirect('reporte_list')
    else:
        form = CambiarEstadoForm(instance=reporte)

    return render(request, 'reportes/cambiar_estado.html', {'form': form, 'reporte': reporte})




