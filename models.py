from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    group_id: Mapped[int] = mapped_column('group_id', Integer,
                                          ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    group: Mapped['Group'] = relationship(Group, backref='students')


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    teacher_id: Mapped[int] = mapped_column('teacher_id', Integer,
                                            ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    teacher: Mapped['Teacher'] = relationship(Teacher, backref='subjects')


class Mark(Base):
    __tablename__ = 'marks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    created: Mapped[Date] = mapped_column('created', Date, nullable=True)
    student_id: Mapped[int] = mapped_column('student_id', Integer,
                                            ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject_id: Mapped[int] = mapped_column('subject_id', Integer,
                                            ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    student: Mapped['Student'] = relationship(Student, backref='marks')
    subject: Mapped['Subject'] = relationship(Subject, backref='marks')
