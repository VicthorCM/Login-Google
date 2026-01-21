from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        sociallogin.state['next'] = '/api/token/'
        return user

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    
    # Este método é quem decide para onde ir após o login com sucesso
    def get_login_redirect_url(self, request):
        # Aqui você retorna a URL que deseja.
        # Pode ser hardcoded '/api/token/' ou usar reverse()
        return '/api/token/'