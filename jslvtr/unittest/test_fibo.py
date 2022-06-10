from unittest import TestCase

from jslvtr.unittest.fibonacci import fibonacci


class TestFibo(TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")

    def setUp(self):
        print("setUp..")

    def test_negativo(self):
        print("test...")
        # with self.assertRaises(Exception):    # toma todas las excepciones
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_cero(self):
        print("test...")
        value = 0
        expected = 1
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_uno(self):
        print("test...")
        value = 1
        expected = 1
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_cinco(self):
        print("test...")
        value = 5
        expected = 8
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_diez(self):
        print("test...")
        value = 10
        expected = 89
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def test_treinta(self):
        print("test...")
        value = 30
        expected = 1346269
        result = fibonacci(value)
        self.assertEqual(result, expected)

    def tearDown(self):
        print("tearDown..\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass.")