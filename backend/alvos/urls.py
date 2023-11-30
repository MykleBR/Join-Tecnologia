from django.urls import path
from .views import lista_alvos, detalhe_alvo, cria_alvo, atualiza_alvo, exclui_alvo

urlpatterns = [
    path('alvos/', lista_alvos, name='lista_alvos'),
    path('alvos/<int:alvo_id>/', detalhe_alvo, name='detalhe_alvo'),
    path('alvos/cria/', cria_alvo, name='cria_alvo'),
    path('alvos/atualiza/<int:alvo_id>/', atualiza_alvo, name='atualiza_alvo'),
    path('alvos/exclui/<int:alvo_id>/', exclui_alvo, name='exclui_alvo'),
]
