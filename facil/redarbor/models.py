from datetime import datetime
from . import db

db.create_all()
class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    # user info
    Email = db.Column(db.String(50), nullable=False) 
    Fax = db.Column(db.String(9), nullable=False)  
    Name = db.Column(db.String(50), nullable=True)
    Telephone = db.Column(db.String(9), nullable=False)

    # metadata
    CreatedOn = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    UpdatedOn = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    DeletedOn = db.Column(db.DateTime(), nullable=True, default=db.func.current_timestamp())
    Lastlogin = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    # login
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

    # busines data
    CompanyId = db.Column(db.Integer, nullable=False)
    PortalId = db.Column(db.Integer, nullable=False)
    RoleId = db.Column(db.Integer, nullable=False)
    StatusId = db.Column(db.Integer, nullable=False)
    
    # def __init__(self, dict):
    #     self.Email = dict.get('email', '')
    #     self.Fax = dict.get('fax', '')
    #     self.Name = dict.get('name', '')
    #     self.Telephone = dict.get('telephone', '')
    #     self.Username = dict.get('username', '')
    #     self.Password = dict.get('password', '')
    #     self.CompanyId = dict.get('companyId')
    #     self.PortalId = dict.get('portalId', '')
    #     self.RoleId = dict.get('roleId', '')
    #     self.StatusId = dict.get('statusId', '')
        
    def save(self):
        print('id:', id)
        if not self.id:
            db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()