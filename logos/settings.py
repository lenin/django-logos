from django.conf import settings

DEFAULT_LOGO_URL = getattr(settings, 'DEFAULT_LOGO_URL', '')
LOGO_UPLOAD_TO = getattr(settings, 'LOGO_UPLOAD_TO', 'logos')
