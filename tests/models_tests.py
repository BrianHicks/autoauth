'tests for models'
from django.test import TestCase
from django.contrib.auth.models import User
from milkman.dairy import milkman

from datetime import datetime

from autoauth.models import AuthToken

from hashlib import sha1

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
