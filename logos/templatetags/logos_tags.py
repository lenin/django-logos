from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Library, Node, TemplateSyntaxError

from logos.models import Logo
from logos.settings import DEFAULT_LOGO_URL

register = Library()

class GetLogoNode(Node):
    def __init__(self, asvar):
        self.asvar = asvar

    def __repr__(self):
        return "<GetLogoNode>"

    def render(self, context):
        try:
            logo = Logo.on_site.filter(is_active=True).latest()
        except Logo.DoesNotExist:
            logo_url = DEFAULT_LOGO_URL
            if not (logo_url.startswith('/') or logo_url.startswith('http://')):
                logo_url = "%s%s" % (settings.MEDIA_URL, logo_url)
            current_site = Site.objects.get_current()
            logo = {
                'title': '[Logo %s]' % current_site.name,
                'image': {'url': logo_url}
            }

        context[self.asvar] = logo
        return ''

def get_logo(parser, token):
    bits = token.split_contents()
    if len(bits) != 3:
        raise TemplateSyntaxError("%r expected format is 'as name'" % bits[0])
    if bits[1] != "as":
        raise TemplateSyntaxError("%r expected format is 'as name'" % bits[0])
    asvar = bits[2]

    return GetLogoNode(asvar)
get_logo = register.tag(get_logo)
