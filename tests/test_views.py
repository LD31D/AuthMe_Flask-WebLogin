import unittest

from views import app


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../tests/test.db'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login(self):
        response = self.app.get('/login/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

        response = self.app.post(
            '/login/', 
            data={
                'login': 'test',
                'password': 'password'
            })

        self.assertIn(b'Invalid login or password', response.data)

        response = self.app.post(
            '/login/', 
            data={
                'login': '',
                'password': ''
            })

        self.assertIn(b'Fields shouldn&#39;t be empty', response.data)

        response = self.app.post(
            '/login/', 
            data={
                'login': 'test',
                'password': '12345678'
            })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'<a href="/">/</a>', response.data)
