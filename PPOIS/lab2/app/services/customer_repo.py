import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.orm_model import Customer


class CustomersRepository:
    def __init__(self, db_connect: DbConnect) -> None:
        self.db_connect = db_connect
        self.session_maker = db_connect.get_sessionmaker()

    def get_all(self):
        s = self.session_maker()
        customers = s.query(Customer.fullname, Customer.account_number,
                            Customer.address, Customer.landline, Customer.mobile).all()
        s.close()
        return customers

    def get_filtered(self, options):
        s = self.session_maker()
        customers = s.query(
            Customer.fullname,
            Customer.account_number,
            Customer.address,
            Customer.landline,
            Customer.mobile
        ).filter(
            Customer.fullname.contains(options.fullname),
            Customer.account_number.contains(options.account_number),
            Customer.address.contains(options.address),
            or_(Customer.mobile.contains(options.phone),
                Customer.landline.contains(options.phone))
        ).all()
        s.close()
        return customers

    def save(self, customer: Customer):
        s = self.session_maker()
        s.add(customer)
        s.commit()
        s.close()

    def delete_customers(self, to_delete: List):
        s = self.session_maker()
        print(to_delete)
        sql1 = delete(Customer).where(Customer.account_number.in_(to_delete))
        s.execute(sql1)
        s.commit()
        s.close()
