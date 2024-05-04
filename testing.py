# program untuk login
class LoginSystem:
    def __init__(self):
        self.users = {"user1": "password1",
                      "user2": "password2"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

# pengujian manual
login_system = LoginSystem()
print(login_system.login("user1", "password1"))  # Harusnya menghasilkan True
print(login_system.login("user1", "wrongpassword"))  # Harusnya menghasilkan False

# pengujian otomatis
import unittest

class TestLoginSystem(unittest.TestCase):
    def setUp(self):
        self.login_system = LoginSystem()

    def test_login_success(self):
        self.assertTrue(self.login_system.login("user1", "password1"))

    def test_login_fail(self):
        self.assertFalse(self.login_system.login("user1", "wrongpassword"))

if __name__ == "__main__":
    unittest.main()
