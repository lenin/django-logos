from django.conf import settings
from django.template import Library, Node, TemplateSyntaxError

from logos.models import Logo
from logos.settings import DEFAULT_LOGO_URL

register = Library()

class LogoURLNode(Node):
    def __init__(self, asvar):
        self.asvar = asvar

    def __repr__(self):
        return "<LogoURLNode>"

    def render(self, context):
        try:
            logo_url = Logo.on_site.filter(is_active=True).latest().image.url
        except Logo.DoesNotExist:
            logo_url = DEFAULT_LOGO_URL
            if not (logo_url.startswith('/') or logo_url.startswith('http://')):
                logo_url = "%s%s" % (settings.MEDIA_URL, logo_url)

        if self.asvar:
            context[self.asvar] = logo_url
            return ''
        else:
            return logo_url

def logo_url(parser, token):
    bits = token.split_contents()
    if len(bits) > 3:
        raise TemplateSyntaxError("%r takes at most two arguments" % bits[0])

    asvar = None
    if len(bits) > 1:
        if bits[1] != "as":
            raise TemplateSyntaxError("%r expected format is 'as name'" % bits[0])
        asvar = bits[2]

    return LogoURLNode(asvar)
logo_url = register.tag(logo_url)
