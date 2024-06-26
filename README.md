# Sistem Login dan Pengujian

Program ini adalah tugas dari mata kuliah Implementasi dan Pengujian Perangkat Lunak. Tugasnya adalah membuat program yang mengimplementasikan pengujian manual dan otomatis menggunakan bahasa Python.

## Sistem Login

Sistem login adalah kelas yang memiliki fungsi login. Fungsi ini akan memeriksa apakah username dan password yang diberikan cocok dengan yang ada di database pengguna.

```python
class LoginSystem:
    def __init__(self):
        self.users = {"user1": "password1",
                      "user2": "password2"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
```

## Pengujian Manual

Pengujian manual dilakukan dengan mencetak hasil dari fungsi login.

```python
login_system = LoginSystem()
print(login_system.login("user1", "password1"))  # Harusnya menghasilkan True
print(login_system.login("user1", "wrongpassword"))  # Harusnya menghasilkan False
```

## Pengujian Otomatis

Pengujian otomatis dilakukan dengan menggunakan modul `unittest` dari Python. Kelas `TestLoginSystem` memiliki dua metode pengujian: `test_login_success` dan `test_login_fail`.

```python
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
```