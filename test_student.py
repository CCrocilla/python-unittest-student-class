""" Imports """
import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

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

    def test_apply_extension(self):
        """ Check for Extension in the End Date """
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(
            self.student.end_date, old_end_date + timedelta(days=5))

    # Mocking Tests is used to test external factors without using them.
    def test_course_schedule_success(self):
        """ Check for Success Mock Request """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_fail(self):
        """ Check for Fail Mock Request """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")


if __name__ == '__main__':
    unittest.main()
