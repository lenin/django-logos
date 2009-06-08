from datetime import datetime

from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

class Logo(models.Model):
    image = models.ImageField(upload_to='logos')
    is_active = models.BooleanField(default=True)
    upload_date = models.DateTimeField(default=datetime.now, editable=False)
    site = models.ManyToManyField(Site, editable=False)

    objects = models.Manager()
    on_site = CurrentSiteManager()

    class Meta:
        get_latest_by = 'upload_date'
        ordering = ('is_active', '-upload_date')

    def save(self, force_insert=False, force_update=False):
        created = not self.id
        super(Logo, self).save(force_insert, force_update)
        if created:
            self.site.add(Site.objects.get_current())
