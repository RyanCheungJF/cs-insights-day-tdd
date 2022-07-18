from unittest import TestCase

from insights.quarter import to_quarter


class Test(TestCase):
    def test_january(self):
        self.assertEqual('Q1', to_quarter(1))
