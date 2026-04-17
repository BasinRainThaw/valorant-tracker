import unittest

from valorant_tracker.render import *


class RenderTest(unittest.TestCase):

    def test_decode_session(self):
        self.assertEqual(decode_session({}), {})
