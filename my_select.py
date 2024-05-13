from sqlalchemy import func, desc, and_

from config import session, engine
from models import Subject, Student, Mark, Group, Teacher, Base
from seed import fake_tables


def select_1():
    result = (
        session.query(
            Student.id,
            Student.name,
            func.round(func.avg(Mark.mark)).label('average_mark')
        )
        .select_from(Student)
        .join(Mark)
        .group_by(Student.id)
        .order_by(desc('average_mark'))
        .limit(5)
    ).all()

    return result


def select_2():
    result = (
        session.query(
            Student.id,
            Student.name,
            Subject.name,
            func.round(func.avg(Mark.mark)).label('average_mark')
        )
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .group_by(
            Student.id,
            Student.name,
            Subject.name)
        .order_by(desc('average_mark'))
        .limit(1)
    ).all()

    return result


def select_3():
    result = (
        session.query(
            Group.name.label('group_name'),
            Subject.name.label('subject_name'),
            func.round(func.avg(Mark.mark)).label('average_mark')
        )
        .select_from(Subject)
        .join(Mark)
        .join(Student)
        .join(Group)
        .where(Subject.id == 2)
        .group_by(
            Group.name,
            Subject.name)
        .order_by(desc('average_mark')
                  )).all()

    return result


def select_4():
    result = (session.query(func.round(func.avg(Mark.mark).label('average_mark'))).select_from(Mark)).all()

    return result


def select_5():
    result = (
        session.query(
            Teacher.id.label('teacher_id'),
            Teacher.name.label('teacher_name'),
            Subject.name.label('subject_name')
        )
        .select_from(Teacher)
        .join(Subject)
        .where(Teacher.id == 1)
        .order_by(
            Teacher.id,
            Teacher.name,
            Subject.name
        )).all()

    return result


def select_6():
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Group.id.label('group_id'),
            Group.name.label('group_name')
        )
        .select_from(Student)
        .join(Group)
        .where(Group.id == 3)
        .order_by(
            Student.id,
            Student.name,
            Group.id,
            Group.name
        )).all()

    return result


def select_7():
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Group.id.label('group_id'),
            Group.name.label('group_name'),
            Subject.id.label('subject_id'),
            Subject.name.label('subject_name'),
            Mark.mark
        )
        .select_from(Student)
        .join(Group)
        .join(Mark)
        .join(Subject)
        .where(and_(
            Group.id == 1,
            Subject.id == 3)
        )
        .order_by(
            Subject.id,
            Subject.id
        )).all()

    return result


def select_8():
    result = (
        session.query(
            Teacher.id.label('teacher_id'),
            Teacher.name.label('teacher_name'),
            Subject.id.label('subject_id'),
            Subject.name.label('subject_name'),
            func.round(func.avg(Mark.mark)).label('average_mark')
        )
        .select_from(Teacher)
        .join(Subject)
        .join(Mark)
        .where(Teacher.id == 3)
        .group_by(
            Teacher.id,
            Teacher.name,
            Subject.id,
            Subject.name)
        .order_by('average_mark')).all()

    return result


def select_9():
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Subject.id.label('subject_id'),
            Subject.name.label('subject_name')
        )
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .group_by(
            Student.id,
            Student.name,
            Subject.id,
            Subject.name
        )).all()

    return result


# SAWarning
def select_10():
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Teacher.id.label('teacher_id'),
            Teacher.name.label('teacher_name'),
            Subject.id.label('subject_id'),
            Subject.name.label('subject_name')
        )
        .select_from(Student, Teacher)
        .join(Subject)
        .where(and_(Student.id == 7, Teacher.id == 1))
        .group_by(
            Student.id,
            Student.name,
            Teacher.id,
            Teacher.name,
            Subject.id,
            Subject.name
        )).all()

    return result


def select_11():
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Teacher.id.label('teacher_id'),
            Teacher.name.label('teacher_name'),
            func.round(func.avg(Mark.mark).label('average_mark'))
        )
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .join(Teacher)
        .where(and_(Teacher.id == 1, Student.id == 17))
        .group_by(
            Student.id,
            Student.name,
            Teacher.id,
            Teacher.name)
    ).all()

    return result


def select_12():
    subquery = (
        session.query(
            Mark.student_id,
            Mark.subject_id,
            func.max(Mark.created).label('max_created')
        )
        .group_by(Mark.student_id, Mark.subject_id)
        .subquery()
    )
    result = (
        session.query(
            Student.id.label('student_id'),
            Student.name.label('student_name'),
            Group.id.label('group_id'),
            Group.name.label('group_name'),
            Subject.id.label('subject_id'),
            Subject.name.label('subject_name'),
            Mark.mark,
            Mark.created
        )
        .join(Mark, Mark.student_id == Student.id)
        .join(Group, Group.id == Student.group_id)
        .join(Subject, Subject.id == Mark.subject_id)
        .join(
            subquery,
            and_(
                Mark.student_id == subquery.c.student_id,
                Mark.subject_id == subquery.c.subject_id,
                Mark.created == subquery.c.max_created
            )
        )
        .filter(Group.id == 3)
        .filter(Subject.id == 3)
    ).all()

    return result


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    fake_tables()
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())
    print(select_11())
    print(select_12())
