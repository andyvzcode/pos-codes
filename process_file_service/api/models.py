from django.db import models


class PosCodes(models.Model):
    lat = models.TextField(blank=True, null=True)
    lng = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    inserted_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.pk)
