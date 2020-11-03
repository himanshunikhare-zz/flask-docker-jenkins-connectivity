from app import app
import unittest

class FlaskTest(unittest.TestCase):

    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/posts")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check for content
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/posts")
        print(response.content_type)
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    
if __name__ == "__main__":
    unittest.main()