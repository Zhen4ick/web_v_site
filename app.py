from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY']="123123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Маршрут регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Имя пользователя уже занято.')
            return redirect(url_for('register'))

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно. Теперь вы можете войти.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Маршрут входа

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/b1')
def b1():
    return render_template('b1.html')

@app.route('/b2')
def b2():
    return render_template('b2.html')

@app.route('/b3')
def b3():
    return render_template('b3.html')

@app.route('/b4')
def b4():
    return render_template('b4.html')
@app.route('/g1')
def g1():
    return render_template('g1.html')
@app.route('/g2')
def g2():
    return render_template('g2.html')

@app.route('/g3')
def g3():
    return render_template('g3.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)