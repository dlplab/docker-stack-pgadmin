import os

ENHANCED_COOKIE_PROTECTION = True
SESSION_COOKIE_SECURE = True

AUTHENTICATION_SOURCES = ['oauth2', 'internal']
OAUTH2_AUTO_CREATE_USER = True

_authentik_url = os.environ['AUTHENTIK_URL']

OAUTH2_CONFIG = [
    {
        'OAUTH2_NAME': 'authentik',
        'OAUTH2_DISPLAY_NAME': 'authentik',
        'OAUTH2_CLIENT_ID': os.environ['OAUTH_CLIENT_ID'],
        'OAUTH2_CLIENT_SECRET': os.environ['OAUTH_CLIENT_SECRET'],
        'OAUTH2_TOKEN_URL': f'{_authentik_url}/application/o/token/',
        'OAUTH2_AUTHORIZATION_URL': f'{_authentik_url}/application/o/authorize/',
        'OAUTH2_API_BASE_URL': f'{_authentik_url}/',
        'OAUTH2_USERINFO_ENDPOINT': f'{_authentik_url}/application/o/userinfo/',
        'OAUTH2_SERVER_METADATA_URL': f'{_authentik_url}/application/o/pgadmin/.well-known/openid-configuration',
        'OAUTH2_SCOPE': 'openid email profile',
        'OAUTH2_USERNAME_CLAIM': 'email',
        'OAUTH2_ICON': 'fa-openid',
        'OAUTH2_BUTTON_COLOR': '#fd4b2d',
    }
]
