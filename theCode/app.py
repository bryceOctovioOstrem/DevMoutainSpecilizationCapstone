import os
from pickle import EMPTY_LIST
from flask import Flask, render_template
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user, login_required,logout_user
from Forms import LoginForm, RegistrationForm, monsterForm, searchForm
from werkzeug.security import generate_password_hash, check_password_hash
from model import User, monsters
from base import app, db

app.config['SECRET_KEY'] = 'mysecretkey'
db.create_all()

@app.route("/",methods=['GET','POST'])
def input():
    form = monsterForm()

    if form.validate_on_submit():
        new_alien =  monsters(author = form.author.data,monster_name = form.monster_name.data,experience = form.experience.data,size = form.Size.data,initative = form.initative.data ,perception= form.preception.data,hp = form.hp.data,Eac = form.AC.data,Kac = form.AC.data,Fort = form.Fort.data,senses = form.senses.data,reflexes = form.reflexes.data,will =form.will.data,defensive_abilities = form.defensive_abilities.data,immunities = form.immunities.data,speed = form.speed.data,melee = form.melee.data,ranged = form.Ranged.data,statistics = form.statistics.data,skills =form.skills.data,languges = form.languges.data,gear = form.treasure.data,space = form.author.data, organization = form.organization.data)
        db.session.add(new_alien)
        db.session.commit()
        

    return render_template("input.html",form=form)

@app.route('/search_monster',methods=['GET','POST'])
def search_monster():
    form = searchForm()
    if form.validate_on_submit():
        monsterWanted = monsters.query.filter_by(monster_name=form.monster_name.data).first()
        return render_template('search_monster.html',monsterWanted= monsterWanted,form=form)
    else:
        monsterWanted = []
        return render_template('search_monster.html',monsterWanted= monsterWanted,form=form)



# @app.route("/static,<filename>")
# def Static(filename):
#     return send_from_directory("static", filename)

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you logged out!")
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if  user is not None and user.check_password(form.password.data) :

            login_user(user)
            flash('logged in success')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            
            return redirect(next)
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,username=form.username.data,password= form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
