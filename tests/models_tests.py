'tests for models'
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from hashlib import sha1
from milkman.dairy import milkman
from mock import patch

from autoauth.models import AuthToken


class SaveTests(TestCase):
    'test saving an AuthToken'
    def tearDown(self):
        'remove any AuthTokens'
        AuthToken.objects.all().delete()

    def test_sets_hash(self):
        'saving an AuthToken sets its hash'
        user = milkman.deliver(User)
        now = datetime.now()

        token = AuthToken(
            user=user,
            expires=now,
        )
        token.save()

        self.assertEqual(
            sha1(now.isoformat() + str(user.pk)).hexdigest(),
            token.hash
        )

    @patch('autoauth.models.datetime')
    def test_sets_expires(self, mock_dt):
        'saving AuthToken sets its expire date'
        now = datetime.now()
        mock_dt.now.return_value = now
        user = milkman.deliver(User)

        token = AuthToken(
            user=user,
        )
        token.save()

        self.assertEqual(
            token.expires,
            now + timedelta(days=1)
        )

    @patch('autoauth.models.datetime')
    @patch('autoauth.models.settings')
    def test_sets_expires_setting(self, mock_settings, mock_dt):
        'expire date is set based on settings.AUTOAUTH_EXPIRY'
        now = datetime.now()
        mock_dt.now.return_value = now

        offset = timedelta(hours=1)
        mock_settings.AUTOAUTH_EXPIRY = offset

        user = milkman.deliver(User)

        token = AuthToken(
            user=user,
        )
        token.save()

        self.assertEqual(
            token.expires,
            now + offset
        )
