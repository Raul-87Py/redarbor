from datetime import datetime
from . import db

db.create_all()
class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    # user info
    Email = db.Column(db.String(50), nullable=False) 
    Fax = db.Column(db.String(9), nullable=True)  
    Name = db.Column(db.String(50), nullable=True)
    Telephone = db.Column(db.String(9), nullable=True)

    # metadata
    CreatedOn = db.Column(db.DateTime(), nullable=True, default=db.func.current_timestamp())
    UpdatedOn = db.Column(db.DateTime(), nullable=True, default=db.func.current_timestamp())
    DeletedOn = db.Column(db.DateTime(), nullable=True, default=db.func.current_timestamp())
    Lastlogin = db.Column(db.DateTime(), nullable=True, default=db.func.current_timestamp())

    # login
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

    # busines data
    CompanyId = db.Column(db.Integer, nullable=False)
    PortalId = db.Column(db.Integer, nullable=False)
    RoleId = db.Column(db.Integer, nullable=False)
    StatusId = db.Column(db.Integer, nullable=False)
 

    def __init__(self, dict):
        self.Email = dict.get('email', '')
        self.Fax = dict.get('fax', '')
        self.Name = dict.get('name', '')
        self.Telephone = dict.get('telephone', '')
        self.Username = dict.get('username', '')
        self.Password = dict.get('password', '')
        self.CompanyId = dict.get('companyId')
        self.PortalId = dict.get('portalId', '')
        self.RoleId = dict.get('roleId', '')
        self.StatusId = dict.get('statusId', '')
        
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Employee.query.order_by(Employee.id).all()

    @staticmethod
    def get_by_id(id):
        return Employee.query.get(id)

    @staticmethod
    def update_by_id(id, dict):
        db.session.update(id).values(dict)
        # query = db.update(emp).values(salary = 100000)
        db.session.commit()
        # return Employee.query.get(id)
        