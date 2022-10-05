from base import db , app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
#from base import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(db.Model,UserMixin): 

    __tablename__ = 'users'

    id= db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash =db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
    
class monsters(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.Text)
    monster_name = db.Column(db.Text)
    experience = db.Column(db.Integer)
    size = db.Column(db.Text)
    initative = db.Column(db.Text)
    perception = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    Eac = db.Column(db.Integer)
    Kac = db.Column(db.Integer)
    Fort = db.Column(db.Integer)
    senses = db.Column(db.Text)
    reflexes = db.Column(db.Integer)
    will = db.Column(db.Integer)
    defensive_abilities = db.Column(db.Text)
    immunities = db.Column(db.Text)
    speed = db.Column(db.Integer)
    melee = db.Column(db.Text)
    ranged = db.Column(db.Text)
    statistics = db.Column(db.Text)
    skills = db.Column(db.Text)
    languges = db.Column(db.Text)
    gear = db.Column(db.Text)
    space = db.Column(db.Text)
    organization = db.Column(db.Text)

    def __init__(self,monster_name,author,experience,size,initative,perception,hp,Eac, Kac,Fort,senses,reflexes,will,defensive_abilities,immunities,speed,melee,ranged,statistics,skills,languges,gear,space,organization):
        self.author = author
        self.monster_name = monster_name
        self.experience = experience
        self.size = size
        self.initative = initative
        self.perception = perception
        self.hp = hp
        self.Eac = Eac
        self.Kac = Kac
        self.Fort = Fort
        self.senses = senses
        self.reflexes = reflexes
        self.will = will
        self.defensive_abilities = defensive_abilities
        self.immunities = immunities
        self.speed = speed
        self.melee = melee
        self.ranged = ranged
        self.statistics = statistics
        self.skills = skills
        self.gear = gear
        self.organization = organization
        self.languges = languges

db.create_all()