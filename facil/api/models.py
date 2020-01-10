from datetime import datetime

from . import db
from .utilities import response_helper

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
    UpdatedOn = db.Column(db.DateTime(), nullable=True, onupdate=db.func.current_timestamp())
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
        self.Email = dict.get('Email', '')
        self.Fax = dict.get('Fax', '')
        self.Name = dict.get('Name', '')
        self.Telephone = dict.get('Telephone', '')
        self.Username = dict.get('Username', '')
        self.Password = dict.get('Password', '')
        self.CompanyId = dict.get('CompanyId')
        self.PortalId = dict.get('PortalId', '')
        self.RoleId = dict.get('RoleId', '')
        self.StatusId = dict.get('StatusId', '')
        
    def add(self):
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
        try:
            Employee.query.filter_by(id = int(id)).update(dict)
            db.session.commit() 
            response = response_helper(True, msg="SUCCES")
            
        except Exception as e:
            response = response_helper(False, msg="ERROR", error=str(e))

        return response

    @staticmethod
    def delete_by_id(id):
        Employee.query.filter_by(id = int(id)).delete()
        db.session.commit()

    
