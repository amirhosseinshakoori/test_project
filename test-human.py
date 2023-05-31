import unittest
from human import User, Manager


class TestUserMethods(unittest.TestCase):

    def test_validate_password(self):
        self.assertTrue(User.validate_password("abcde"))
        self.assertTrue(User.validate_password("abcd"))
        self.assertFalse(User.validate_password("abc"))

    def test_register_user(self):
        user = User('test', '09123456789', '1234')
        self.assertTrue(user.register_user(self))

    def test_edit_personal_info(self):
        user = User('test', '09123456789', '1234')
        User.register_user(user)
        user.edit_personal_info(new_name='new_test')
        self.assertEqual(user.name, 'new_test')

    def test_login_user(self):
        user = User('test', '09123456789', '1234')
        User.register_user(user)
        logged_in_user = User.login_user('test', '1234')
        self.assertEqual(logged_in_user.name, user.name)

    def test_change_password(self):
        user = User('test', '09123456789', '1234')
        User.register_user(user)
        old_password = user.password
        user.change_password('1234', '4321')
        self.assertNotEqual(old_password, user.password)

    def test_apply_discount(self):
        discount_rate = User.apply_discount('1990-01-01', '2021-01-01')
        self.assertGreaterEqual(discount_rate, 0)
        self.assertLessEqual(discount_rate, 0.3)

    def test_register_admin(self):
        admin = Manager('admin', '09122222222', '1234')
        self.assertTrue(admin.register_admin())

    def test_login_admin(self):
        admin = Manager('admin', '09122222222', '1234')
        Manager.register_admin(admin)
        logged_in_admin = Manager.login_admin('admin', '1234')
        self.assertEqual(logged_in_admin.name, admin.name)

    def test_show_user(self):
        Manager.show_user()

    def test_del_user(self):
        user = User('test', '09123456789', '1234')
        User.register_user(user)
        self.assertTrue(Manager.del_user(user.name))
