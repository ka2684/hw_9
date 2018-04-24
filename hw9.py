from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)


@app.route('/')
def inspiration():
    x=randint(1,20)
    with open("inspiration.txt","r") as f:
        content = f.readlines()
    return render_templates('temp.html', content = context[x]) 


