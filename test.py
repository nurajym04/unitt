import unittest

from calc import add, subtract,  multiplay, divad
print()

class TestAddFunc(unittest.TestCase):
    """
    проверка модуля 
    """

    def test_add_integers(self):
        result = add(25, 7)
        self.assertEqual(result, 32)

    def test_add_floats(self):
        result = add(10.5, 3.3)
        self.asserEqual(result, 13.8)

    def test_add_string(self):
        result = add('фыв', 'йцу')
        self.assertTupleEqual(result, 'фывйцу')


if __name__ 