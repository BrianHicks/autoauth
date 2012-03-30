'models for autoauth'
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models

from hashlib import sha1

from autoauth.conf import default

class AuthTokenManager(models.Manager):
    'auth token model manager'

class AuthToken(models.Model):
    'auth token model'
    expires = models.DateTimeField()
    used = models.BooleanField(default=False)
    hash = models.CharField(max_length=40)
    user = models.ForeignKey('auth.User')

    objects = AuthTokenManager()

    def save(self, *args, **kwargs):
        'save this instance'
        if self.expires is None:
            offset = getattr(
                settings, 'AUTOAUTH_EXPIRY', default.AUTOAUTH_EXPIRY
            )
            self.expires = datetime.now() + offset

        if self.hash == '':
            self.hash = sha1(
                self.expires.isoformat() + str(self.user.pk)
            ).hexdigest()

        super(AuthToken, self).save(*args, **kwargs)
