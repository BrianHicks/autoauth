'models for autoauth'
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models

from hashlib import sha1

class AuthToken(models.Model):
    'auth token model'
    expires = models.DateTimeField()
    used = models.BooleanField(default=False)
    hash = models.StringField(max_length=40)
    user = models.ForeignKey('django.contrib.auth.User')

    def save(self, *args, **kwargs):
        'save this instance'
        if self.expires is None:
            offset = getattr(
                settings, 'AUTOAUTH_EXPIRY', default.AUTOAUTH_EXPIRY
            )
            self.expires = datetime.today + offset

        if self.hash is None:
            self.hash = sha1(
                self.expires.isoformat() + str(user.pk)
            ).hexdigest()

        super(AuthToken, self).save(*args, **kwargs)
