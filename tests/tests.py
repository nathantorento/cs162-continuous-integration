import unittest
import requests
from sqlalchemy import create_engine

URI = 'postgresql://cs162_user:cs162_password@db/cs162'
engine = create_engine(URI)

db = SQLAlchemy(app)

class TestCase(unittest.TestCase):

    def test_connection(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(200, response.status_code)

    def test_post(self):
        response = requests.post('http://localhost:5000/add', data={'expression':'1+1'})
        self.assertEqual(200, response.status_code)

    def test_err(self):
        response = requests.post('http://localhost:5000/add', data={'expressions':'1+1'})
        self.assertEqual(400, response.status_code)

    def test_db(self):
        with engine.connect() as connection:
            result = connection.execute("select * from expression")
        print(result)

if __name__ == '__main__':
    unittest.main()
