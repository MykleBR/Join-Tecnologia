from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import Alvo
import json

def lista_alvos(request):
    alvos = Alvo.objects.all()
    return JsonResponse({'alvos': list(alvos.values())})

@csrf_exempt
def cria_alvo(request):
    if request.method == 'POST':
        # Obtém os dados JSON da requisição POST
        data = json.loads(request.body.decode('utf-8'))

        # Extraia os campos do JSON (nome, latitude, longitude)
        nome = data.get('nome', '')
        latitude = data.get('latitude', 0)
        longitude = data.get('longitude', 0)

        # Calcula a data de expiração (um ano a partir da data atual)
        data_expiracao = datetime.now() + timedelta(days=365)

        # Crie uma instância do modelo Alvo e salve no banco de dados
        alvo = Alvo.objects.create(nome=nome, latitude=latitude, longitude=longitude, data_expiracao=data_expiracao)

        # Retorne uma resposta JSON
        return JsonResponse({'mensagem': 'Alvo criado com sucesso!', 'alvo_id': alvo.id})
    else:
        # Se a requisição não for do tipo POST, retorne um erro
        return JsonResponse({'erro': 'Requisição inválida. Apenas métodos POST são suportados.'}, status=400)

@csrf_exempt
def exclui_alvo(request, alvo_id):
    # Buscar o alvo pelo ID ou retornar 404 se não existir
    alvo = get_object_or_404(Alvo, id=alvo_id)

    # Lógica para excluir o alvo
    alvo.delete()

    return JsonResponse({'mensagem': 'Alvo excluído com sucesso!'})

def detalhe_alvo(request, alvo_id):
    alvo = get_object_or_404(Alvo, pk=alvo_id)
    return JsonResponse({'alvo': model_to_dict(alvo)})

@csrf_exempt
def atualiza_alvo(request):
    if request.method == 'POST':
        # Lógica para atualizar um alvo existente
        print('c* do bilu')
        return JsonResponse({'mensagem': 'Alvo atualizado com sucesso!'})
