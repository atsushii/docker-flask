import unittest
from app import create_app

class TestEndPoint(unittest.TestCase):
    
    def setUp(self):
        print("setup")
        app = create_app()
        self.client = app.test_client()
    
    def tearDown(self):
        print("Complete test")
    
    def test_sample_endpoint(self):
        response = self.client.get("/")

        assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()
