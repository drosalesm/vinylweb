from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', indexPage,name='list'),  
    path('', views.indexPage,name='inicio'),
    path('configuraciones/', views.configuraciones,name='configuraciones'),
    path('catalogo/', views.catalogo_beats,name='catalogo'),
    path('catalogo_vivo/', views.catalogo_live,name='catalogo_vivo'),
    path('ingreso_vinyl/', views.logueo,name='ingreso_vinyl'),
    #--------URLs de navegacion
    path('list_nav/',views.listNavBar.as_view(),name='list_nav'),
    path('crea_nav/',views.NavBarCreateView.as_view(), name='crea_nav'),
    path('upd_nav/<int:pk>', views.navUpdateView.as_view(),name='upd_nav'),
    path('borr_nav/<int:pk>', views.navDeleteView.as_view(),name='borr_nav'),
   #--------URLs de navegacion
    path('list_track/',views.listTracks.as_view(),name='list_track'),
    path('crea_track/',views.tracksCreateView.as_view(), name='crea_track'),
    path('upd_track/<int:pk>', views.tracksUpdateView.as_view(),name='upd_track'),
    path('borr_track/<int:pk>', views.tracksDeleteView.as_view(),name='borr_track'),   
  #--------URLs para la biografia 
    path('list_bio/',views.listBio.as_view(),name='list_bio'),
    path('crea_bio/',views.bioCreateView.as_view(), name='crea_bio'),
    path('upd_bio/<int:pk>', views.bioUpdateView.as_view(),name='upd_bio'),
    path('borr_bio/<int:pk>', views.bioDeleteView.as_view(),name='borr_bio'),   
  #--------URLs para la informacion de contacto 
    path('list_contact/',views.listContact.as_view(),name='list_contact'),
    path('crea_contact/',views.contactCreateView.as_view(), name='crea_contact'),
    path('upd_contact/<int:pk>', views.contactUpdateView.as_view(),name='upd_contact'),
    path('borr_contact/<int:pk>', views.contactDeleteView.as_view(),name='borr_contact'),
  #--------URLs para la informacion de la seccion en vivo 
    path('list_vivo/',views.listEnVivo.as_view(),name='list_vivo'),
    path('crea_vivo/',views.enVivoCreateView.as_view(), name='crea_vivo'),
    path('upd_vivo/<int:pk>', views.enVivoUpdateView.as_view(),name='upd_vivo'),
    path('borr_vivo/<int:pk>', views.enVivoDeleteView.as_view(),name='borr_vivo'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)