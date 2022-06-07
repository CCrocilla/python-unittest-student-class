""" Imports """
import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """ Tests """

    @classmethod
    def setUpClass(cls):
        """ Create Files and Folder just once that the class is called """
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """ This will iterate just once at the end that the class is called """
        print('tearDownClass')

    def setUp(self):
        """ Used as setup to create files and folders each time """
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        """
        Used to close everything.
        This will close after each iteration of the function
        """
        print('tearDown')

    def test_full_name(self):
        """ Check for Student Full Name """
        # student = Student('John', 'Doe') Removed because added in the setUp.
        # Required to add self. in the assertion.

        self.assertEqual(self.student.full_name, 'John Doe')

    def test_email(self):
        """ Check for Student Email """
        # student = Student('John', 'Doe') Removed because added in the setUp.
        # Required to add self. in the assertion.

        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        """ Check for Alert Santa Function """
        # student = Student('John', 'Doe') Removed because added in the setUp.
        # Required to add self. in the assertion.
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


if __name__ == '__main__':
    unittest.main()
