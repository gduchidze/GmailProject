import yagmail
import time
import pandas
import csv
import random
from datetime import datetime, timedelta

auditories = ['201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212']

random.shuffle(auditories)


class Student:
    def __init__(self, name, lastname, university, date, time):
        self.name = name
        self.lastname = lastname
        self.university = university
        self.auditory = random.choice(auditories)
        self.place = random.randint(1, 25)
        self.date = date
        self.time = time

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    @fullname.setter
    def fullname(self, name):
        result = name.split()
        self.name = result[0]
        self.lastname = result[1]

    @property
    def email(self):
        return f'{self.name.lower()}.{self.lastname.lower()}@{self.university.lower()}.edu.ge'

    def get_university(self):
        return self.university


class Person(Student):
    def __init__(self, name, lastname, university, person_count, date, time):
        super().__init__(name, lastname, university, date, time)
        self._person_count = person_count

    @property
    def email(self):
        return f'{self.name.lower()}.{self.lastname.lower()}.{self._person_count}@{self.get_university().lower()}.edu.ge'


exam_date = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
exam_time = datetime.strptime("08:00", "%H:%M") + timedelta(minutes=random.randint(0, 600))
exam_time = exam_time.strftime("%H:%M")

st1 = Person('giorgi', 'duchidze', 'btu', 1, exam_date, exam_time)
st2 = Person('demetre', 'natidze', 'btu', 1, exam_date, exam_time)
st3 = Person('demetre', 'natidze', 'btu', 2, exam_date, exam_time)

data = [
    ['name', 'lastname', 'university', 'email', 'auditory', 'place', 'date', 'time'],
    [st1.name, st1.lastname, st1.university, st1.email, st1.auditory, st1.place, st1.date, st1.time],
    [st2.name, st2.lastname, st2.university, st2.email, st2.auditory, st2.place, st2.date, st2.time],
    [st3.name, st3.lastname, st3.university, st3.email, st3.auditory, st3.place, st3.date, st3.time]
]

with open('names.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

desired_time = datetime.strptime("2024-02-17 2:05", "%Y-%m-%d %H:%M")
current_time = datetime.now()
time_difference = (desired_time - current_time).total_seconds()

if time_difference > 0:
    time.sleep(time_difference)

sender = 'giorgiduchidze2004@gmail.com'

subject = "Exam In Python"
yag = yagmail.SMTP(user=sender, password='YourPassword')
df = pandas.read_csv('names.csv')
for index, row in df.iterrows():
    content = f"""Hello {row['name']}, You Have Exam in Python auditory:{row['auditory']}, place:{row['place']}, Data and Time:{row['date']} on {row['time']},  """
    yag.send(to=row['email'], subject=subject, contents=content)
    print("Email sent!")
print(df)
