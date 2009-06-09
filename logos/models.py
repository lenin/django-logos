from datetime import datetime

from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.translation import ugettext_lazy as _

from logos.settings import LOGO_UPLOAD_TO

class Logo(models.Model):
    image = models.ImageField(_('image'), upload_to=LOGO_UPLOAD_TO)
    is_active = models.BooleanField(_('is active'), default=True)
    upload_date = models.DateTimeField(_('upload date'), default=datetime.now, editable=False)
    site = models.ManyToManyField(Site, verbose_name=_('site'), editable=False)

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        get_latest_by = 'upload_date'
        ordering = ('-is_active',)

    def __unicode__(self):
        return self.image.name[:30]

    def save(self, force_insert=False, force_update=False):
        created = not self.id
        super(Logo, self).save(force_insert, force_update)
        if created:
            self.site.add(Site.objects.get_current())
