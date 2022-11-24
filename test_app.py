import unittest
from fastapi.testclient import TestClient
from app import app, get_transformer_and_model
from utils import generate_dataset
from random import choice

DATASET_SIZE = 20

class TestApp(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        self.client = TestClient(app)

    def test_predict_simple(self):
        get_transformer_and_model()
        for request in generate_dataset(1):
            response = self.client.post('/predict',
                                        json=request)
            print(response.content)
            self.assertEqual(response.status_code, 200)

    def test_predict_several(self):
        get_transformer_and_model()
        for request in generate_dataset(DATASET_SIZE):
            response = self.client.post('/predict',
                                        json=request)
            self.assertEqual(response.status_code, 200)

    def test_predict_error_several(self):
        get_transformer_and_model()
        for request in generate_dataset(DATASET_SIZE):
            field = choice(list(request.keys()))
            request[field] += 1000
            response = self.client.post('/predict',
                                        json=request)
            self.assertEqual(response.status_code, 440)

if __name__ == '__main__':
    unittest.main()