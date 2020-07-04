from app import app
from flask import json
import unittest


class AppTest(unittest.TestCase):

    #check the status code
    def test_statusCode200_surprise(self):
        tester = app.test_client(self)
        res= tester.get("/api/surprise?name=Ayan%20Gosling&birth_year=2000")
        statusCode = res.status_code
        self.assertEqual(statusCode, 200)

    def test_statusCode200_stats(self):
        tester = app.test_client(self)
        res= tester.get("/api/stats")
        statusCode = res.status_code
        self.assertEqual(statusCode, 200)

    def test_statusCode404(self):
        tester = app.test_client(self)
        res= tester.get("/api/surprise?name=Ziva&birth_year=2002")
        statusCode = res.status_code
        self.assertEqual(statusCode, 404)

    def test_statusCode400(self):
        tester = app.test_client(self)
        res= tester.get("/api/surprise?name=Ayan%20Gosling")
        statusCode = res.status_code
        self.assertEqual(statusCode, 400)

    # check if the return value is json
    def test_json_surprise(self):
        tester = app.test_client(self)
        res= tester.get("/api/surprise?name=Ayan%20Gosling&birth_year=2000")
        contentType = res.content_type
        self.assertEqual(contentType, "application/json")

    def test_json_stats(self):
        tester = app.test_client(self)
        res = tester.get("/api/stats")
        contentType = res.content_type
        self.assertEqual(contentType, "application/json")

    # check data responed
    def test_data_chack(self):
        tester = app.test_client(self)
        res = tester.get("/api/surprise?name=Ayan%20Gosling&birth_year=2000")
        self.assertTrue(b'chuck-norris-joke' in res.data)

    def test_data_kanye(self):
        tester = app.test_client(self)
        res = tester.get("/api/surprise?name=Bee%20Gosling&birth_year=2002")
        self.assertTrue(b'kanye-quote' in res.data)
    
    def test_data_nameSum(self):
        tester = app.test_client(self)
        res = tester.get("/api/surprise?name=Ayan%20Gosling&birth_year=2002")
        self.assertTrue(b'name-sum' in res.data)


    def test_data_dogs(self):
        tester = app.test_client(self)
        res = tester.get("/api/surprise?name=Ayan%20Gosling&birth_year=2022")
        self.assertTrue(b'Suprising Dog!' in res.data)


    def test_data_stats(self):
        tester = app.test_client(self)
        res = tester.get("/api/stats")
        data = json.loads(res.get_data(as_text=True))
        self.assertEqual(data['requests'] , 4)
        distribution = data['distribution']
        self.assertEqual(distribution[0]['count'] , 1)
        self.assertEqual(distribution[1]['count'] , 1)
        self.assertEqual(distribution[2]['count'] , 1)

        tester.get("/api/surprise?name=Bee%20Gosling&birth_year=2000")
        res = tester.get("/api/stats")
        data = json.loads(res.get_data(as_text=True))
        distribution = data['distribution']
        self.assertEqual(data['requests'] , 5)
        for d in distribution:
            if d['type'] == 'chuck-norris-joke': 
                self.assertEqual(d['count'] , 2)


    

if __name__ == "__main__":
    unittest.main()