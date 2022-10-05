
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from applications.landing.models import *
from applications.landing.forms import *

# Create your views here.
def indexPage(request):
    opc_nav = nav_bar_opt.objects.order_by('posicion').all()
    list_tracks = tracks.objects.order_by('-lanzamiento')[:9]
    list_vivo = en_vivo.objects.order_by('-fecha_grabacion')[:9]
    bio = biografia.objects.all()
    contact=contacto.objects.all()
    return render(request,'landing/inicio.html',{'opc_nav':opc_nav,'list_tracks':list_tracks,'bio':bio,'contact':contact,'list_vivo':list_vivo})

def configuraciones(request):
    return render(request,'landing/setup.html')

def catalogo_beats(request):
    opc_nav = nav_bar_opt.objects.order_by('posicion').all()
    list_tracks = tracks.objects.order_by('lanzamiento').all()    
    return render(request,'landing/catalog_beats.html',{'opc_nav':opc_nav,'list_tracks':list_tracks})

def catalogo_live(request):
    opc_nav = nav_bar_opt.objects.order_by('posicion').all()
    list_vivo = en_vivo.objects.order_by('-fecha_grabacion')
    return render(request,'landing/catalog_live.html',{'opc_nav':opc_nav,'list_vivo':list_vivo})


def logueo(request):
    return render(request, 'landing/login.html')


#Vistas para crear dinamicamente las opciones del navbar

#@method_decorator(login_required, name='dispatch')
class listNavBar(ListView):
    model = nav_bar_opt
    ordering = ['posicion']    


#@method_decorator(login_required, name='dispatch')
class NavBarCreateView(CreateView):
    form_class = opt_navbar_form
    model = nav_bar_opt
    success_url = '/list_nav'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


#@method_decorator(login_required, name='dispatch')
class navUpdateView(UpdateView):
    form_class = opt_navbar_form
    model = nav_bar_opt
    success_url = '/list_nav'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

#@method_decorator(login_required, name='dispatch')
class navDeleteView(DeleteView):
    model = nav_bar_opt
    success_url = '/list_nav'


# -------------------vistas para el mantenimiento de tracks

#@method_decorator(login_required, name='dispatch')
class listTracks(ListView):
    model = tracks
    ordering = ['-lanzamiento']    


#@method_decorator(login_required, name='dispatch')
class tracksCreateView(CreateView):
    form_class = tracks_form
    model = tracks
    success_url = '/list_track'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


#@method_decorator(login_required, name='dispatch')
class tracksUpdateView(UpdateView):
    form_class = tracks_form
    model = tracks
    success_url = '/list_track'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

#@method_decorator(login_required, name='dispatch')
class tracksDeleteView(DeleteView):
    model = tracks
    success_url = '/list_track'



# -------------------vistas para el mantenimiento de la biografia

#@method_decorator(login_required, name='dispatch')
class listBio(ListView):
    model = biografia

#@method_decorator(login_required, name='dispatch')
class bioCreateView(CreateView):
    form_class = bio_form
    model = biografia
    success_url = '/list_bio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


#@method_decorator(login_required, name='dispatch')
class bioUpdateView(UpdateView):
    form_class = bio_form
    model = biografia
    success_url = '/list_bio'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

#@method_decorator(login_required, name='dispatch')
class bioDeleteView(DeleteView):
    model = biografia
    success_url = '/list_bio'




# -------------------vistas para el mantenimiento de la informacion de contacto

#@method_decorator(login_required, name='dispatch')
class listContact(ListView):
    model = contacto

#@method_decorator(login_required, name='dispatch')
class contactCreateView(CreateView):
    form_class = contact_form
    model = contacto
    success_url = '/list_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


#@method_decorator(login_required, name='dispatch')
class contactUpdateView(UpdateView):
    form_class = contact_form
    model = contacto
    success_url = '/list_contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

#@method_decorator(login_required, name='dispatch')
class contactDeleteView(DeleteView):
    model = contacto
    success_url = '/list_contact'



# -------------------vistas para el mantenimiento de la seccion en vivo



#@method_decorator(login_required, name='dispatch')
class listEnVivo(ListView):
    model = en_vivo

#@method_decorator(login_required, name='dispatch')
class enVivoCreateView(CreateView):
    form_class = vivo_form
    model = en_vivo
    success_url = '/list_vivo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


#@method_decorator(login_required, name='dispatch')
class enVivoUpdateView(UpdateView):
    form_class = vivo_form
    model = en_vivo
    success_url = '/list_vivo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context

#@method_decorator(login_required, name='dispatch')
class enVivoDeleteView(DeleteView):
    model = en_vivo
    success_url = '/list_vivo'
