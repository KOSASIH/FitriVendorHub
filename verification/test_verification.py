import unittest
from.models import User, Verification

class VerificationTestCase(unittest.TestCase):
    def test_verification_code(self):
        user = User(username='test', email='test@example.com')
        verification = Verification(user_id=user.user_id, code='123456')
        self.assertEqual(verification.code, '123456')

    def test_send_verification_code(self):
        user = User(username='test', email='test@example.com')
        send_verification_code.delay(user.user_id)
        # implement test for sending verification code logic here
        pass
