import unittest

from valorant_tracker.auth import *


class AuthTest(unittest.TestCase):

    def test_retry_bucket(self):
        self.assertEqual(retry_bucket({}), {})
