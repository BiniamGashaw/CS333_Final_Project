import unittest
from user import User

class TestUser(unittest.TestCase):

    def test_user_creation(self):
        user = User("Alice")
        self.assertEqual(user.name, "Alice")

    def test_add_to_history(self):
        user = User("Bob")
        user.add_to_history("Addition", 9)
        self.assertEqual(user.history, [("Addition", 9)])

if __name__ == '__main__':
    unittest.main()
