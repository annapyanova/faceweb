from flask import render_template, request
from app import app

name = "(введи своё имя, солнце)"
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
            'author': {'username': 'Аня'},
            'body': 'Куда будем ставить микроволновку?'
        },
        {
            'author': {'username': 'Инга'},
            'body': 'Поставим к нам в комнату'
        }, 
        {
            'author': {'username': 'Сабина'},
            'body': 'В тумбочку!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='Sign In')
