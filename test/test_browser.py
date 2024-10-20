from data.users import student
from pages.registration_pages import RegistrationStudent


def test_registration_student():
    registration_student = RegistrationStudent()

    registration_student.open('https://demoqa.com/automation-practice-form')
    registration_student.register(student)
    registration_student.should_have_registered(student)
