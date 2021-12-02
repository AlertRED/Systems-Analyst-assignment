from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://postgres:@localhost/Fabric')
Session = sessionmaker(engine)
session = Session()


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    employees = relationship("Employee", uselist=True, back_populates="company")

    def __repr__(self):
        return f'{self.name}'


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    fio = Column(String(50))
    birthday = Column(DateTime)
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", uselist=False, back_populates="employees")

    def __repr__(self):
        return f'{self.fio}, {self.company}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)
