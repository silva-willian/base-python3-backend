import unittest
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Bem-vindo à API!")

    def test_receive_data_missing_fields(self):
        data = {}
        response = self.app.post('/api/receive_data', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("field1' é obrigatório", response.data)
        self.assertIn("'field2' é obrigatório", response.data)

    def test_receive_data_valid_data(self):
        data = {'field1': 'value1', 'field2': 'value2'}
        response = self.app.post('/api/receive_data', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"success", response.data)
        self.assertIn(b"value1", response.data)
        self.assertIn(b"value2", response.data)

if __name__ == '__main__':
    unittest.main()
