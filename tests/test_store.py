import unittest

from valorant_tracker.store import *


class StoreTest(unittest.TestCase):

    def test_load_batch(self):
        self.assertEqual(load_batch({}), {})
