from pages.registration_pages import RegistrationStudent


def test_registration_student():
    registration_student = RegistrationStudent()

    registration_student.open('https://demoqa.com/automation-practice-form')
    registration_student.fill_first_name('Anna')
    registration_student.fill_last_name('Ivanova')
    registration_student.fill_email('abc@ya.ru')
    registration_student.fill_gender()
    registration_student.fill_number('8111111111')
    registration_student.fill_date_of_birth('08', 7, 2000)
    registration_student.fill_subject('Chemistry')
    registration_student.fill_hobby()
    registration_student.fill_image('image.png')
    registration_student.fill_current_address('homeland')
    registration_student.fill_state_and_city()
    registration_student.fill_submit()

    # проверки

    registration_student.shoud_have_text('Anna Ivanova',
                                         'abc@ya.ru',
                                         'Female',
                                         '8111111111',
                                         '08 August,2000',
                                         'Chemistry',
                                         'Sports, Music',
                                         'image.png',
                                         'homeland',
                                         'Uttar Pradesh Merrut')
