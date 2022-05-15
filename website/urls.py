from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.introducao_page_view, name='introducao'),
    path('automatos', views.automatos_page_view, name='automatos'),
    path('maquinasturing', views.maquinaturing_page_view, name='maquinasturing'),
    path('nova/', views.novo_automato_view, name='novo'),
    path('edita/<int:automato_id>', views.edita_automato_view, name='edita'),
    path('apaga/<int:automato_id>', views.apaga_automato_view, name='apaga'),
    path('validar/<int:automato_id>', views.validar, name= 'validar'),
    path('detalhes/<int:automato_id>', views.detalhes_page_view, name= 'detalhes'),
    path('novaTM/', views.nova_maquinaturing_view, name='novaTM'),
    path('editaTM/<int:turing_id>', views.edita_maquinaturing_view, name='editaTM'),
    path('apagaTM/<int:turing_id>', views.apaga_maquinaturing_view, name='apagaTM'),
    path('validarTM/<int:turing_id>', views.validarTM, name= 'validarTM'),
    path('detalhesTM/<int:turing_id>', views.detalhes_maquinaturing_view, name='detalhesTM'),
    path('upload/', views.uploadJSON, name= 'upload'),
    path('uploadTM/', views.uploadJSON_TM, name='uploadTM'),
]