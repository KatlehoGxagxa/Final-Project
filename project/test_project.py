# Author: Katleho Gxagxa
# This program writes tests for the project.py file of our application.
from registration import Registration
from service import bus_schedule, deposit, order_ride
from userlogin import LOGIN
import csv
import pytest
from project import menu, main_menu, service_menu


def test_menu():
    expected_output = '''
    ================================
               Welcome!
    ================================
    1. Create New Account
    2. Log In to Existing Account
    3. Exit
    ================================
    '''
    assert menu() == expected_output


@pytest.mark.skip(reason="Have not figured out how to test functions taking input")
def test_main_menu():
    assert True

@pytest.mark.skip(reason="Have not figured out how to test functions taking input")
def test_service_menu():
    assert True