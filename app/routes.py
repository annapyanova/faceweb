from flask import render_template, request
from app import app

name = "(Введите своё имя)"
@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    global name
    username = request.form.get("username")
    if username==None:
          user = {'username':name}
    else:
          user = {'username':username}
          name = username
    posts = [
        {
            'author': {'username': 'Note'},
            'body': 'Данный сервис предназначен для автоматического трекинга объектов. Пожалуйста, загрузите свое видео:'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')

@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html', title='Download')
