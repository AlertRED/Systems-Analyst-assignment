from datetime import datetime
from random import randint

from model import Company, Employee, Session


def random_date():
    return datetime.date(datetime.fromtimestamp(randint(0, 1000000000)))


if __name__ == '__main__':
    with Session() as session:
        for i in range(1, 11):
            company = Company(name=f'Company {i}')
            session.add(company)
            for j in range(1, 11):
                employee = Employee(fio=f'fio {i}-{j}', company=company, birthday=random_date())
                session.add(employee)
        session.commit()
