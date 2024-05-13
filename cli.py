import argparse

from sqlalchemy import update, delete, func

from config import session
from models import Group, Student, Teacher, Subject, Mark


# Teacher
def create_teacher(teacher_name: str):
    new_teacher = Teacher(name=teacher_name)
    session.add(new_teacher)
    session.commit()


def read_teachers():
    teachers = session.query(Teacher.name).all()

    return teachers


def update_teacher(teacher_id: int, teacher_name: str):
    teacher = update(Teacher).where(Teacher.id == teacher_id).values(name=teacher_name)
    session.execute(teacher)
    session.commit()


def delete_teacher(teacher_id: int):
    teacher = delete(Teacher).where(Teacher.id == teacher_id)
    session.execute(teacher)
    session.commit()


# Group
def create_group(group_name: str):
    new_group = Group(name=group_name)
    session.add(new_group)
    session.commit()


def read_groups():
    groups = session.query(Group.name).all()

    return groups


def update_group(group_id: int, group_name: str):
    group = update(Group).where(Group.id == group_id).values(name=group_name)
    session.execute(group)
    session.commit()


def delete_group(group_id: int):
    group = delete(Group).where(Group.id == group_id)
    session.execute(group)
    session.commit()


# Student
def create_student(student_name: str):
    random_group_id = session.query(Group).order_by(func.random()).first()
    new_student = Student(name=student_name, group_id=random_group_id.id)
    session.add(new_student)
    session.commit()


def read_students():
    students = session.query(Student.name).all()

    return students


def update_student(student_id: int, student_name: str):
    student = update(Student).where(Student.id == student_id).values(name=student_name)
    session.execute(student)
    session.commit()


def delete_student(student_id: int):
    student = delete(Student).where(Student.id == student_id)
    session.execute(student)
    session.commit()


# Subject
def create_subject(subject_name: str):
    random_teacher_id = session.query(Teacher).order_by(func.random()).first()

    new_subject = Subject(name=subject_name, teacher_id=random_teacher_id.id)
    session.add(new_subject)
    session.commit()


def read_subjects():
    subjects = session.query(Subject.name).all()

    return subjects


def update_subject(subject_id: int, subject_name: str):
    subject = update(Subject).where(Subject.id == subject_id).values(name=subject_name)
    session.execute(subject)
    session.commit()


def delete_subject(subject_id: int):
    subject = delete(Subject).where(Subject.id == subject_id)
    session.execute(subject)
    session.commit()


# Mark
def read_marks():
    marks = session.query(Mark.mark).all()

    return marks


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='University',
        description='CRUD for University database',
        epilog='')
    parser.add_argument('--action', '-a', choices=['create', 'list', 'update', 'remove'],
                        help='create, list, update, remove')
    parser.add_argument('--model', '-m', choices=['Teacher', 'Group', 'Student', 'Subject', 'Mark'],
                        help='Teacher, Group, Student, Subject, Mark')
    parser.add_argument('--id', type=int, help='Id')
    parser.add_argument('--name', '-n', help='name')
    args = parser.parse_args()

    actions_map = {
        'create': {
            'Teacher': create_teacher,
            'Group': create_group,
            'Student': create_student,
            'Subject': create_subject
        },
        'list': {
            'Teacher': read_teachers,
            'Group': read_groups,
            'Student': read_students,
            'Subject': read_subjects,
            'Mark': read_marks
        },
        'update': {
            'Teacher': update_teacher,
            'Group': update_group,
            'Student': update_student,
            'Subject': update_subject
        },
        'remove': {
            'Teacher': delete_teacher,
            'Group': delete_group,
            'Student': delete_student,
            'Subject': delete_subject
        },
    }

    args_map = {
        'create': (args.name,),
        'list': (),
        'update': (args.id, args.name),
        'remove': (args.id,)
    }

    print(actions_map[args.action][args.model](*args_map[args.action]))
