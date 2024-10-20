import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: str
    date_of_birth: dict[str, int]
    subject: str
    hobby: str
    image: str
    address: str
    state: str


student = User(
    first_name='Anna',
    last_name='Ivanova',
    email='abc@ya.ru',
    gender='Female',
    number='8111111111',
    date_of_birth={"day": "08", "month": 7, "year": "2000", "month2": "August"},
    subject='Chemistry',
    hobby='Sports, Music',
    image='image.png',
    address='homeland',
    state='Uttar Pradesh Merrut'
)
