import unittest
from  pitch.models import Post

class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(username = 'Zephon', password = 'testing')
    def test_password_setter(self):
        self.assertTrue(self.new_post.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_post.password

    def test_password_verification(self):
        self.assertTrue(self.new_post.verify_password('testing'))