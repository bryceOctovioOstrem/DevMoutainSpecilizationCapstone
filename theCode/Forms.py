from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from model import User
 
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit= SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first:
            raise ValidationError('Username is taken!')

class monsterForm(FlaskForm):
    author = StringField('author')
    monster_name = StringField('monster_name')
    challange_rating = StringField('challange_rating')
    experience = IntegerField('experience')
    Size = StringField('Size')
    initative = StringField('initative')
    preception = StringField('preception')
    hp = IntegerField('hp')
    AC = IntegerField('AC')
    description = StringField('description')
    Fort = IntegerField('Fort')
    senses = StringField('senses')
    reflexes = IntegerField('reflexes')
    defensive_abilities = StringField('defensive_abilities')
    immunities = StringField('immunities')
    speed = StringField('speed')
    melee = StringField('melee')
    statistics = StringField('statistics')
    skills = StringField('skills')
    languges = StringField('languges')
    treasure = StringField('treasure')
    organization = StringField('organization')
    will = IntegerField('will')
    Ranged = StringField('ranged')
    submit = SubmitField("submit monster")



class searchForm(FlaskForm):
    monster_name = StringField('monster_name')
    submit = SubmitField("search monster")