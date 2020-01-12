from datetime import datetime

from . import db


class EmployeeModel(db.Model):

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
    DeletedOn = db.Column(db.DateTime(), nullable=True)
    Lastlogin = db.Column(db.DateTime(), nullable=True)

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
        
    def add_data(self):
        if not self.id:
            db.session.add(self)
        db.session.commit() 
        return self.id



    @staticmethod
    def get_all():
        return EmployeeModel.query.order_by(EmployeeModel.id).all()

    @staticmethod
    def get_by_id(id):
        return EmployeeModel.query.get(int(id))

    # @staticmethod
    def update_by_id(id, dict):
        EmployeeModel.query.filter_by(id = int(id)).update(dict)
        db.session.commit()

    @staticmethod
    def delete_by_id(id):
        EmployeeModel.query.filter_by(id = int(id)).delete()
        db.session.commit()