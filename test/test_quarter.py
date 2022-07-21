from unittest import TestCase

from insights.quarter import to_quarter


class Test(TestCase):
    def test_to_quarter_validMonth(self):
        dateDict = {
            1: 'Q1',
            2: 'Q1',
            3: 'Q1',
            4: 'Q2',
            5: 'Q2',
            6: 'Q2',
            7: 'Q3', 
            8: 'Q3', 
            9: 'Q3',
            10: 'Q4', 
            11: 'Q4',
            12: 'Q4' 
        }
        for k, v in dateDict.items():
            with self.subTest(f'to_quarter({k}) = {v}'):
                self.assertEqual(v, to_quarter(k))

    def test_to_quarter_invalidMonth(self):
        self.assertRaises(Exception, to_quarter, 0)
