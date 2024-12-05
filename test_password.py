import unittest

from user_management import _is_valid_password


class TestPassword(unittest.TestCase):
    def test_username_as_password(self):
        username = 'username'
        password = username
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_weak_password(self):
        username = 'username'
        password = 'password'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_short_password(self):
        username = 'username'
        password = '32sysc!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_long_password(self):
        username = 'username'
        password = 'thisisaverylongpassword2!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_upper(self):
        username = 'username'
        password = 'alllower1!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_lower(self):
        username = 'username'
        password = 'ALLUPPERCASE2!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_lower(self):
        username = 'username'
        password = 'ALLUPPER2!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_number(self):
        username = 'username'
        password = 'NoNumber!'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_special_character(self):
        username = 'username'
        password = 'MyPassword1'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertFalse(is_valid_password)

    def test_password_with_no_number(self):
        username = 'username'
        password = 'Xy!6Dwp8'
        is_valid_password, error = _is_valid_password(username, password)
        self.assertTrue(is_valid_password)


if __name__ == '__main__':
    unittest.main()
