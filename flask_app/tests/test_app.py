import unittest
from flask_app.app import calculate, app

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("2 + 3"), 5)
        self.assertEqual(calculate("10+5"), 15)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            calculate("2++3")
        with self.assertRaises(ValueError):
            calculate("")

    def test_operands(self):
        with self.assertRaises(ValueError):
            calculate("a + 3")
        with self.assertRaises(ValueError):
            calculate("4 + b")


class TestFlaskRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<html', response.data.lower())

    def test_post_valid_expression(self):
        response = self.client.post('/', data={'display': '2 + 3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'5', response.data)

    def test_post_invalid_expression(self):
        response = self.client.post('/', data={'display': '2++3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error:', response.data)


if __name__ == '__main__':
    unittest.main()
