from random import randint

from model import Company, Employee, session
from datetime import datetime, date


def find_user(fio: str, company_name: str):
    company = session.query(Company).filter_by(name=company_name).one()
    if not company:
        raise "Company doesn't found"
    employee = session.query(Employee).filter_by(fio=fio, company=company).one()
    if not employee:
        raise "User doesn't found"
    return employee


def count_users_from_company(company_name: str):
    company = session.query(Company).filter_by(name=company_name).one()
    if not company:
        raise "Company doesn't found"
    return len(company.employees)


def get_birthdays(birthday: date):
    employees = session.query(Employee).filter_by(birthday=birthday).all()
    return employees


if __name__ == '__main__':
    print(find_user('fio -1', 'Company 1'))
    print(count_users_from_company('Company 1'))
    birthday = datetime.date(datetime.fromtimestamp(randint(0, 1000000000)))
    print(get_birthdays(birthday))
