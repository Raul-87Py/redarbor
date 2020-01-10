from datetime import datetime
from . import db


class Employee(db.Model):
    __tablename__ = 'employee'

    # user info
    Email = db.Column(db.String(50), nullable=False) 
    Fax = db.Column(db.String(9), nullable=False)  
    Name = db.Column(db.String(50), nullable=False)
    Telephone = db.Column(db.String(9), nullable=False)

    # metadata
    CreatedOn = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    UpdatedOn = db.Column(db.DateTime(), nullable=False)
    DeletedOn = db.Column(db.DateTime(), nullable=True)
    Lastlogin = db.Column(db.DateTime(), nullable=False)

    # login
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

    # busines data
    CompanyId = db.Column(db.Integer, primary_key=True)
    PortalId = db.Column(db.Integer, nullable=False)
    RoleId = db.Column(db.Integer, nullable=False)
    StatusId = db.Column(db.Integer, nullable=False)
    
    def __init__(self, dict):

        self.Email = dict.get('email', '')
        self.Fax = dict.get('fax', '')
        self.Fame = dict.get('name', '')
        self.Telephone = dict.get('telephone', '')
        self.Username = dict.get('username', '')
        self.Password = dict.get('password', '')
        self.CompanyId = dict.get('companyId')
        self.PortalId = dict.get('portalId', '')
        self.RoleId = dict.get('roleId', '')
        self.StatusId = dict.get('statusId', '')
        
    def insert():
        db.session.add(new_user)
        db.session.commit()