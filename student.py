""" Imports """
from datetime import date, timedelta
import requests


class Student:
    """ A Student class as base for method Testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._date_start = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """ Return the Full Name of the Student """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """ Return Student Email """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        """ Built applying Test Driven Development (TDD) """
        self.naughty_list = True

    def apply_extension(self, days):
        """ Extension End Date """
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        response = requests.get(
            f"http://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
