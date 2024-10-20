import os

from selene import browser, be, have
from data.users import User

CURRENT_FILE = os.path.abspath(__file__)
DIRECTORY = os.path.dirname(CURRENT_FILE)
FILE = os.path.join(DIRECTORY, "..", "resources")

class RegistrationStudent:

    def open(self, value):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def register(self, user: User):
        browser.element('#firstName').should(be.blank).type(user.first_name).press_enter()
        browser.element('#lastName').should(be.blank).type(user.last_name).press_enter()
        browser.element('#userEmail').should(be.blank).type(user.email).press_enter()
        browser.element('label[for=gender-radio-2]').click()
        browser.element('#userNumber').should(be.blank).type(user.number).click()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value = "{user.date_of_birth["month"]}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value = "{user.date_of_birth["year"]}"]').click()
        browser.element(f'.react-datepicker__day--0{user.date_of_birth["day"]}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('label[for=hobbies-checkbox-1]').click()
        browser.element('label[for=hobbies-checkbox-3]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(f"{FILE}/{user.image}"))
        browser.element('#currentAddress').should(be.blank).type(user.address).press_enter()
        browser.element('#state').click()
        browser.element('//*[text()="Uttar Pradesh"]').click()
        browser.element('#city').click()
        browser.element('//*[text()="Merrut"]').click()
        browser.element('#submit').click()

    def should_have_registered(self, user: User):
        browser.element('//table//td[contains(text(),"Student Name")]/../td[2]').should(have.text(user.first_name + " " + user.last_name))
        browser.element('//table//td[contains(text(),"Student Email")]/../td[2]').should(have.text(user.email))
        browser.element('//table//td[contains(text(),"Gender")]/../td[2]').should(have.text(user.gender))
        browser.element('//table//td[contains(text(),"Mobile")]/../td[2]').should(have.text(user.number))
        browser.element('//table//td[contains(text(),"Date of Birth")]/../td[2]').should(have.text(user.date_of_birth["day"] + " " + user.date_of_birth["month2"] + "," + user.date_of_birth["year"]))
        browser.element('//table//td[contains(text(),"Subjects")]/../td[2]').should(have.text(user.subject))
        browser.element('//table//td[contains(text(),"Hobbies")]/../td[2]').should(have.text(user.hobby))
        browser.element('//table//td[contains(text(),"Picture")]/../td[2]').should(have.text(user.image))
        browser.element('//table//td[contains(text(),"Address")]/../td[2]').should(have.text(user.address))
        browser.element('//table//td[contains(text(),"State and City")]/../td[2]').should(
            have.text(user.state))









