from django.test import TestCase
from transform_number import transform
import requests


class TestWordToNumber(TestCase):
    def setUp(self):
        self.number1 = 'one'
        self.number2 = 'twenty two'
        self.number3 = 'one hundred fifty seven'

    def test_number(self):
        self.assertEqual(1, transform(self.number1))
        self.assertEqual(22, transform(self.number2))
        self.assertEqual(157, transform(self.number3))


class TestNotEmptyRequest(TestCase):
    def setUp(self):
        self.example1 = 'http://127.0.0.1:8000/api/v1/match-deck/?ship=1&name=three'
        self.example2 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=Acq&ship=2'
        self.example3 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=Nau&ship=2'

    def test_not_empty(self):
        # response = self.client.get(self.example1)
        # response = view(requests)
        rez1 = requests.get(self.example1)
        self.assertEqual(
            '[{"deck":"Deck 3","sort_order":3,"description":"text"}]', rez1.content)
        rez2 = requests.get(self.example2)
        self.assertEqual(
            '[{"deck":"Acquamarina","sort_order":5,"description":"text"},'
            '{"deck":"Acquarius","sort_order":6,"description":"text"}]', rez2.content)
        rez3 = requests.get(self.example3)
        self.assertEqual(
            '[{"deck":"Nautica","sort_order":1,"description":"text"},'
            '{"deck":"Nautica","sort_order":4,"description":"text"}]', rez3.content)


class TestReturnOther(TestCase):

    def setUp(self):
        self.example1 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=NA&ship=1'
        self.example2 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=three&ship=12'
        self.example3 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=-&ship=1'
        self.example4 = 'http://127.0.0.1:8000/api/v1/match-deck/?name=0&ship=12'

    def test_return_other(self):
        rez1 = requests.get(self.example1)
        self.assertEqual(
            '[{"deck":"Other","sort_order":0,"description":"text"}]', rez1.content)
        rez2 = requests.get(self.example2)
        self.assertEqual(
            '[{"deck":"Other","sort_order":0,"description":"text"}]', rez2.content)
        rez3 = requests.get(self.example3)
        self.assertEqual(
            '[{"deck":"Other","sort_order":0,"description":"text"}]', rez3.content)
        rez4 = requests.get(self.example4)
        self.assertEqual(
            '[{"deck":"Other","sort_order":0,"description":"text"}]', rez4.content)