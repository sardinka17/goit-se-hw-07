from random import randint

from faker import Faker

from config import session
from models import Group, Teacher, Subject, Student, Mark

fake = Faker('uk-Ua')


def fake_groups():
    groups = ['A', 'B', 'C']

    for group in groups:
        new_group = Group(name=group)
        session.add(new_group)

    session.commit()


def fake_teachers():
    for _ in range(3):
        new_teacher = Teacher(name=fake.name())
        session.add(new_teacher)

    session.commit()


def fake_subjects():
    subjects = [['English', 'Math'], ['History', 'Biology'], ['Science', 'Music']]

    for teacher_id in range(1, 4):
        for subject_index in range(2):
            new_subject = Subject(name=subjects[teacher_id - 1][subject_index], teacher_id=teacher_id)
            session.add(new_subject)

        session.commit()


def fake_students_and_marks():
    for group_id in range(1, 4):
        for _ in range(10):
            new_student = Student(name=fake.name(), group_id=group_id)
            session.add(new_student)

            student_id = session.query(Student).order_by(Student.id.desc()).first().id

            for subject_id in range(1, 7):
                for _ in range(3):
                    new_mark = Mark(subject_id=subject_id, mark=randint(0, 100), student_id=student_id,
                                    created=fake.date_this_decade())
                    session.add(new_mark)

    session.commit()


def fake_tables():
    fake_groups()
    fake_teachers()
    fake_subjects()
    fake_students_and_marks()
