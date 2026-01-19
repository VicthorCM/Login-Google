from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
    return render(request,"home.html")

@login_required
def login_success_jwt(request):
    # Gera o par de tokens (Access + Refresh) para o usuário logado
    user = request.user
    refresh = RefreshToken.for_user(user)

    return JsonResponse({
        'mensagem': 'Login com Google realizado com sucesso!',
        'usuario': user.email,
        'tokens': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    data = {
        "message": f'Olá {request.user.username}, esse é seu perfil',
        "user": request.user.username,
    }
    return Response(data)

